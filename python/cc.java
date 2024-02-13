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

    private final MediaType mediaType = MediaType.APPLICATION_JSON;
    private final CarService carService;

    public CarController(CarService carService) {
        this.carService = carService;
    }

    @GetMapping
    public Flux<Car> findAll() {
        return carService.findAll();
    }

    @GetMapping("/{id}")
    public Mono<Car> findById(@PathVariable String id) {
        return carService.findById(id);
    }

    @PostMapping
    public Mono<ResponseEntity<Car>> create(@RequestBody Car car) {
        return carService.create(car.getName())
                .map(createdCar -> ResponseEntity.created(URI.create("/car/" + createdCar.getId())).body(createdCar));
    }

    @DeleteMapping("/{id}")
    public Mono<ResponseEntity<Car>> deleteById(@PathVariable String id) {
        return carService.delete(id)
                .map(deletedCar -> ResponseEntity.ok().body(deletedCar))
                .defaultIfEmpty(ResponseEntity.notFound().build());
    }

    @PutMapping("/{id}")
    public Mono<ResponseEntity<Car>> updateById(@PathVariable String id, @RequestBody Car car) {
        return carService.update(id, car.getName())
                .map(updatedCar -> ResponseEntity.ok().body(updatedCar))
                .defaultIfEmpty(ResponseEntity.notFound().build());
    }
}