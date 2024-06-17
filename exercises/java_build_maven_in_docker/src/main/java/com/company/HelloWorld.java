package com.company;

import org.apache.commons.lang3.StringUtils;

public class HelloWorld {
    public static void main(String[] args) {
        String text = "This is a simple Maven app using Apache Commons Lang....";
        String reversed = StringUtils.reverse(text);

        System.out.println("Original: " + text);
        System.out.println("Reversed: " + reversed);
    }
}
