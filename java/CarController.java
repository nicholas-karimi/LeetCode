package com.codility.external;

import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.net.URI;

@RestController
@RequestMapping("/car")
public class CarController {

    private final CarService carService;

    public CarController(CarService carService) {
        this.carService = carService;
    }

    @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
    public Flux<Car> findAll() {
        return carService.findAll();
    }

    @GetMapping(path = "/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public Mono<ResponseEntity<Car>> findById(@PathVariable String id) {
        return carService.findById(id)
                .map(car -> ResponseEntity.ok(car))
                .switchIfEmpty(Mono.just(ResponseEntity.notFound().build()));
    }

    @PostMapping(consumes = MediaType.APPLICATION_JSON_VALUE)
    public Mono<ResponseEntity<Car>> create(@RequestBody Car car) {
        return carService.create(car.getName())
                .map(createdCar -> ResponseEntity.created(URI.create("/car/" + createdCar.getId())).body(createdCar))
                .onErrorResume(error -> Mono.just(ResponseEntity.badRequest().body("Error creating car: " + error.getMessage())));
    }

    @DeleteMapping(path = "/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public Mono<ResponseEntity<Void>> delete(@PathVariable String id) {
        return carService.delete(id)
                .then(Mono.just(ResponseEntity.noContent().build()))
                .onErrorResume(error -> Mono.just(ResponseEntity.notFound().body("Car with ID " + id + " not found")));
    }

    @PutMapping(path = "/{id}", consumes = MediaType.APPLICATION_JSON_VALUE)
    public Mono<ResponseEntity<Car>> update(@PathVariable String id, @RequestBody Car car) {
        car.setId(id);
        return carService.update(car)
                .map(updatedCar -> ResponseEntity.ok(updatedCar))
                .switchIfEmpty(Mono.just(ResponseEntity.notFound().body("Car with ID " + id + " not found")))
                .onErrorResume(error -> Mono.just(ResponseEntity.badRequest().body("Error updating car: " + error.getMessage())));
    }
}
