package com.logicbig.example;

import java.util.Arrays;

public class MyMainClass {
    public static void main(String[] args) {
        Arrays.stream(args).forEach(System.out::println);
    }
}