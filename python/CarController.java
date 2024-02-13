package com.codility.external;

import org.reactivestreams.Publisher;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Mono;

import java.net.URI;

public class CarController {

    private final MediaType mediaType = MediaType.APPLICATION_JSON;
    private final CarService carService;

    public CarController(CarService carService) {
        this.carService = carService;
    }

    public void findAll() {

    }

    public void findById() {

    }

    public void create() {

    }

    public void deleteById() {

    }

    public void updateById() {

    }
}
