package com.company;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AppTest {
    @Test
    void appHasAGreeting() {
        HelloWorld classUnderTest = new HelloWorld();
        assertNotNull(classUnderTest, "app should have a greeting");
    }
}
