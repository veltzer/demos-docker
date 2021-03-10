
* Build java software inside docker using gradle

* Create a docker images based on java on an operating system (and then you need to install java).

* Put gradle inside the docker image you are creating. Use the zip version of installation.

* In the following instructions we are creating a standard hello world Java + gradle project.

* create a java file called HelloWorld.java residing in a folder structure like so:
Gradle build folder inside the docker
└── src
    └── main
        └── java
            └── hello
                └── HelloWorld.java

with the following content:

```java
package hello;

public class HelloWorld {
        public static void main(String[] args) {
                System.out.println("Hello, World!");
        }
}
```

* Add a build.gradle file with the following content:

```gradle
apply plugin: 'java'
```

* When the container runs, make sure to run

```
gradle build
```
