
# Low-Level Design (LLD) Notes for Interviews

## 📌 Object-Oriented Programming (OOP) Concepts

1. **Encapsulation**
   - Binding data and methods that operate on that data within one unit (class).
   - Example:
     ```java
     class Account {
         private double balance;

         public void deposit(double amount) {
             balance += amount;
         }

         public double getBalance() {
             return balance;
         }
     }
     ```

2. **Abstraction**
   - Hiding internal details and showing only essential features.
   - Example:
     ```java
     abstract class Vehicle {
         abstract void start();
     }

     class Car extends Vehicle {
         void start() {
             System.out.println("Car starting");
         }
     }
     ```

3. **Inheritance**
   - Mechanism for creating new classes from existing ones.
   - Example:
     ```java
     class Animal {
         void eat() { System.out.println("Eating"); }
     }

     class Dog extends Animal {
         void bark() { System.out.println("Barking"); }
     }
     ```

4. **Polymorphism**
   - One interface, multiple implementations.
   - Example:
     ```java
     class Animal {
         void sound() { System.out.println("Some sound"); }
     }

     class Cat extends Animal {
         void sound() { System.out.println("Meow"); }
     }

     Animal a = new Cat();
     a.sound(); // Meow
     ```

---

## Composition vs Inheritance

#### Inheritance

**Definition**: "Is-a" relationship. One class inherits the properties and behaviors of another.

**Advantages**
- Reuse of common logic via superclass
- Supports polymorphism

**Disadvantages**
- Tight coupling between base and derived classes
- Inflexible if superclass changes
- Can lead to fragile code and hard-to-maintain hierarchies

**Example**

    class Animal {
        void makeSound() {
            System.out.println("Generic sound");
        }
    }

    class Dog extends Animal {
        void makeSound() {
            System.out.println("Bark");
        }
    }

#### Composition

**Definition**: "Has-a" relationship. One class includes instances of other classes to reuse functionality.

**Advantages**
- Loosely coupled and more modular
- More flexible than inheritance
- Behavior can be changed at runtime

**Disadvantages**
- Requires more boilerplate code
- May introduce extra layers of abstraction

**Example**

    class Engine {
        void start() {
            System.out.println("Engine started");
        }
    }

    class Car {
        private Engine engine = new Engine();

        void drive() {
            engine.start();
            System.out.println("Car is moving");
        }
    }

### Comparison Table

| Feature              | Inheritance         | Composition        |
|----------------------|---------------------|---------------------|
| Relationship         | IS-A                | HAS-A              |
| Coupling             | Tight               | Loose              |
| Flexibility          | Low                 | High               |
| Reusability          | Through subclassing | Through delegation |
| Runtime Behavior     | Static              | Can be dynamic     |
| Ideal Use Case       | Well-defined hierarchies | Behavior reuse without hierarchy |

### When to Prefer Composition

- When flexibility and maintainability are priorities
- When runtime behavior changes are needed
- When a strict hierarchy doesn’t naturally exist

> **Rule of thumb**: Favor composition over inheritance when possible.

---

## 📐 SOLID Principles
[Uncle Bob’s SOLID Principles Made Easy](https://www.youtube.com/watch?v=pTB30aXS77U)

1. **Single Responsibility Principle (SRP)**  
   A class should only have one reason to change. In other words, a class should have only one job or purpose within the software system. 
   - ✅ Separate concerns like persistence, UI, business logic into different classes.  
   - ❌ Don't mix file saving and data transformation logic.

2. **Open/Closed Principle (OCP)**  
   Software entities (classes, modules, functions) should be open for extension but closed for modification which means you should be able to extend a class behavior, without modifying it.   
   - ✅ Use abstract classes/interfaces and extend them.  
   - ❌ Don't modify existing logic to add new features.

3. **Liskov Substitution Principle (LSP)**  
   Subtypes must be substitutable for their base types. This means if you have a base class and a derived class, you should be able to use instances of the derived class wherever instances of the base class are expected, without breaking the application. 
   - ✅ Derived class should not throw unexpected exceptions or break expectations of parent class.  
   - ❌ Avoid "override to do nothing" or throw "NotImplemented" errors.

4. **Interface Segregation Principle (ISP)**  
   No client should be forced to depend on methods it does not use. You should prefer many client interfaces rather than one general interface and each interface should have a specific responsibility.
   - ✅ Split fat interfaces into smaller, more specific ones.  
   - ❌ Avoid large service interfaces with many unused methods.

5. **Dependency Inversion Principle (DIP)**  
   High-level modules should not depend on low-level modules; both should depend on abstractions. DIP suggests that classes should rely on abstractions (e.g., interfaces or abstract classes) rather than concrete implementations. 
   - ✅ Use dependency injection via constructors or frameworks.  
   - ❌ Don’t instantiate concrete classes directly inside classes.

---

## 🧠 GRASP Patterns (General Responsibility Assignment Software Patterns)

GRASP is a set of guidelines for assigning responsibility in object-oriented design. These principles help create maintainable, understandable, and flexible systems.

1. **Information Expert**
- Assign responsibility to the class with the necessary information.
- Promotes encapsulation and low coupling.
- 🔁 Often leads to delegation across multiple small classes.

- **Example**:  
If `Order` needs to calculate total price, it should do it itself because it has the list of `LineItems`.

2. **Creator**
- Who creates a new instance of a class?
- Assign this responsibility to a class that:
  - Contains it
  - Aggregates it
  - Records it
  - Uses it closely
- Promotes low coupling.

- **Example**:  
`Order` creates `LineItem` objects because it aggregates them.

3. **Controller**
- Assign responsibility for handling input system events to a controller object.
- Not the UI, but an intermediate object that handles business logic coordination.
- Often one controller per system use case.

- **Example**:  
`OrderController` handles `placeOrder()` from the UI and delegates to domain objects.

4. **Low Coupling**
- Minimize dependencies between classes.
- Makes classes easier to change, reuse, and test.

- **Example**:  
Use interfaces, dependency injection, and avoid tight dependencies on concrete classes.

5. **High Cohesion**
- Keep related behavior in one place.
- Helps maintain, understand, and reuse code.

- **Example**:  
A `User` class should manage profile updates but not payment logic.

6. **Polymorphism**
- Assign responsibility for behavior based on type variation using polymorphism.

- **Example**:  
`Shape.draw()` is implemented differently by `Circle` and `Rectangle`.

7. **Pure Fabrication**
- Create a class to achieve high cohesion and low coupling, even if it doesn’t represent a real-world concept.

- **Example**:  
A `PersistenceManager` class handles DB storage instead of domain objects doing it themselves.

8. **Indirection**
- Use an intermediate object to mediate interaction between components.
- Supports low coupling.

- **Example**:  
Use a `ServiceLocator` or `EventDispatcher` between a controller and a service.

9. **Protected Variations**
- Design to protect elements from the variations in other elements.
- Use stable interfaces to shield clients from change.

- **Example**:  
Use the `Payment` interface and multiple implementations (`CreditCard`, `PayPal`, etc.).

---

### ✅ GRASP vs SOLID
- **GRASP** focuses on **responsibility assignment**.
- **SOLID** focuses on **class-level design principles**.
- Both aim for maintainable, modular, and scalable object-oriented systems.

---


## 💡 Other Design Principles

- **DRY (Don't Repeat Yourself)**
  - Extract repeated logic into functions/classes.
  - Example: Avoid duplicating validation code in multiple controllers.

- **YAGNI (You Aren't Gonna Need It)**
  - Don’t build functionality until it's necessary.
  - ✅ Only implement "Export to PDF" if a real use case exists.

- **KISS (Keep It Simple, Stupid)**
  - Avoid overengineering. Start with the simplest design that works.
  - ✅ Don’t use Kafka when a method call suffices.

---


## 🎨 Design Pattern Categories

1. **Creational Patterns**
- Focus on object creation mechanisms.
- Examples:
  - **Singleton**: One instance globally.
  - **Factory Method**: Delegate instantiation to subclasses.
  - **Abstract Factory**: Provide interface for creating families of related objects.
  - **Builder**: Step-by-step construction of complex objects.
  - **Prototype**: Clone existing object.

2. **Structural Patterns**
- Deal with object composition.
- Examples:
  - **Adapter**: Convert one interface to another.
  - **Decorator**: Add functionality at runtime.
  - **Facade**: Simplify complex subsystems with a unified interface.
  - **Composite**: Treat individual objects and compositions uniformly.
  - **Proxy**: Control access to an object.

3. **Behavioral Patterns**
- Focus on communication between objects.
- Examples:
  - **Observer**: Notify multiple objects on state change.
  - **Strategy**: Select algorithm at runtime.
  - **Command**: Encapsulate a request as an object.
  - **Chain of Responsibility**: Pass request along a chain.
  - **State**: Allow object to change behavior based on internal state.
  - **Template Method**: Define program skeleton and allow subclasses to modify steps.
  - **Mediator**: Reduce direct communication between objects.

---

## 🧩 Important Design Patterns
[Neetcode - 8 Design Patterns EVERY Developer Should Know](https://www.youtube.com/watch?v=tAuRQs_d9F8)
1. **Singleton**
- Ensures a class has only one instance.
```java
class Singleton {
    private static Singleton instance = null;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) instance = new Singleton();
        return instance;
    }
}
```

2. **Factory Pattern**
- Delegates object creation to a separate method/class.
```java
interface Shape { void draw(); }

class Circle implements Shape {
    public void draw() { System.out.println("Drawing Circle"); }
}

class ShapeFactory {
    static Shape getShape(String type) {
        if (type.equals("circle")) return new Circle();
        return null;
    }
}
```

3. **Strategy Pattern**
- Encapsulate interchangeable behaviors and use delegation.
```java
interface PaymentStrategy { void pay(); }

class PayPal implements PaymentStrategy {
    public void pay() { System.out.println("Paid via PayPal"); }
}

class Checkout {
    private PaymentStrategy strategy;

    Checkout(PaymentStrategy strategy) {
        this.strategy = strategy;
    }

    void processPayment() { strategy.pay(); }
}
```

4. **Observer Pattern**
- Notify multiple observers when a subject changes.
```java
interface Observer { void update(); }

class EmailService implements Observer {
    public void update() { System.out.println("Email sent"); }
}

class Order {
    List<Observer> observers = new ArrayList<>();
    void attach(Observer o) { observers.add(o); }

    void placeOrder() {
        for (Observer o : observers) o.update();
    }
}
```

5. **Decorator Pattern**
- Add functionality without altering the original class.
```java
interface Coffee { int cost(); }

class BasicCoffee implements Coffee {
    public int cost() { return 5; }
}

class MilkDecorator implements Coffee {
    Coffee coffee;

    MilkDecorator(Coffee coffee) { this.coffee = coffee; }

    public int cost() { return coffee.cost() + 2; }
}
```

6. MVC (Model-View-Controller)

- **Model**: Manages the data and business logic.
- **View**: Presents data to the user and handles user interface.
- **Controller**: Accepts user input, invokes model updates, and selects view.

```java
// Model
class User {
    private String name;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}

// View
class UserView {
    public void printUserDetails(String name) {
        System.out.println("User: " + name);
    }
}

// Controller
class UserController {
    private User model;
    private UserView view;

    public UserController(User model, UserView view) {
        this.model = model;
        this.view = view;
    }

    public void setUserName(String name) {
        model.setName(name);
    }

    public void updateView() {
        view.printUserDetails(model.getName());
    }
}
```

7. **Builder Pattern**
- Used to construct complex objects step by step.

```java
class Pizza {
    private String dough;
    private String sauce;
    private String topping;

    public static class Builder {
        private String dough;
        private String sauce;
        private String topping;

        public Builder setDough(String dough) {
            this.dough = dough;
            return this;
        }

        public Builder setSauce(String sauce) {
            this.sauce = sauce;
            return this;
        }

        public Builder setTopping(String topping) {
            this.topping = topping;
            return this;
        }

        public Pizza build() {
            Pizza pizza = new Pizza();
            pizza.dough = this.dough;
            pizza.sauce = this.sauce;
            pizza.topping = this.topping;
            return pizza;
        }
    }
}
```

8. **Iterator Pattern**
- Provides a way to access elements of a collection sequentially without exposing the underlying representation.
```java
interface Iterator {
    boolean hasNext();
    Object next();
}

class NameRepository {
    String[] names = {"Alice", "Bob", "Charlie"};

    public Iterator getIterator() {
        return new NameIterator();
    }

    private class NameIterator implements Iterator {
        int index = 0;

        public boolean hasNext() {
            return index < names.length;
        }

        public Object next() {
            return hasNext() ? names[index++] : null;
        }
    }
}
```

9. **Facade Pattern**
- Provides a simplified interface to a complex system.
```java
class CPU {
    void freeze() {}
    void execute() {}
}

class Memory {
    void load(String position, String data) {}
}

class HardDrive {
    String read(String lba, int size) { return "data"; }
}

class ComputerFacade {
    private CPU cpu;
    private Memory memory;
    private HardDrive hardDrive;

    public ComputerFacade() {
        this.cpu = new CPU();
        this.memory = new Memory();
        this.hardDrive = new HardDrive();
    }

    public void start() {
        cpu.freeze();
        String data = hardDrive.read("0x0000", 1024);
        memory.load("0x0000", data);
        cpu.execute();
    }
}
```

10. **Adapter Pattern**
- Allows incompatible interfaces to work together.
```java
interface MediaPlayer {
    void play(String audioType, String fileName);
}

class AdvancedMediaPlayer {
    void playMp4(String fileName) {
        System.out.println("Playing mp4: " + fileName);
    }
}

class MediaAdapter implements MediaPlayer {
    AdvancedMediaPlayer advancedPlayer = new AdvancedMediaPlayer();

    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("mp4")) {
            advancedPlayer.playMp4(fileName);
        }
    }
}

class AudioPlayer implements MediaPlayer {
    MediaAdapter adapter;

    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("mp3")) {
            System.out.println("Playing mp3: " + fileName);
        } else if (audioType.equalsIgnoreCase("mp4")) {
            adapter = new MediaAdapter();
            adapter.play(audioType, fileName);
        } else {
            System.out.println("Unsupported format");
        }
    }
}
```

---

## 🧭 UML Diagrams

1. **Class Diagram**
[UML Class Diagram Reference](https://www.uml-diagrams.org/class-reference.html)
- Represents classes and relationships.

```text
+---------------+
|    Car        |
+---------------+
| -speed: int   |
+---------------+
| +drive(): void|
+---------------+
        ^
        |
+---------------+
| SportsCar     |
+---------------+
```

2. **Sequence Diagram**
- Represents how objects interact in sequence.

```text
User -> LoginService: login(username, pwd)
LoginService -> DB: validateUser()
DB --> LoginService: result
LoginService --> User: success/failure
```

3. **Use Case Diagram**
- Represents system actors and use cases.

```text
[User] --> (Login)
[User] --> (Browse Products)
[Admin] --> (Add Product)
```

---

## ✅ Tips for LLD Interviews

- Always ask clarifying questions.
- Start with requirements and assumptions.
- Identify key entities and relationships.
- Explain trade-offs and design choices.
- Use interfaces and design patterns.
- Sketch UML diagrams for clarity.
- Think about scale, extensibility, and testability.

---

Also check out this excellent resource for interview problems:  
- [Awsome low level design](https://github.com/ashishps1/awesome-low-level-design/tree/main/problems)