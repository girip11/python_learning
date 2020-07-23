# Command pattern

* Decouples sender and invoker objects.
* Sender objects will be the one creating the commands.
* Command object encapsulates the receiver object and the method/action to execute on that receiver object.
* Invoker object receives the command and executes the command when required.

## Implementation

* Abstract interface/base class for commands with `execute` and `undo` methods.
* `undo` method should be able to reverse the changes done by the command execution.

* Each command object will be given the receiver object and the method that should be executed on the receiver object when `execute` method is called.

* Invoker object will be given the command object. Invoker object will be calling the `execute` method on the command object.

## Example

* [Python example implementation](https://github.com/faif/python-patterns/blob/master/patterns/behavioral/command.py)

## Rule of thumb

* Macro commands can be implemented using composite pattern.
* Undo operation can be implemented using memento.
* Chain of Responsibility can use Command to represent requests as objects.

---

## References

* [Command design pattern](https://sourcemaking.com/design_patterns/command)

* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
