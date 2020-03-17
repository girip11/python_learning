# Aggregation and Composition

* Aggregation and composition are a form of association.

* When object contains other objects as its contents, the association between those objects is either **aggregation** or **composition**

* Aggregation or composition is described with phrase **has a**. Ex: Employee has a salary pay

* The relationship can be either unidirectional or bidirectional.

* The relationship between the objects can be **1-N, N-1 or M-N**

## Composition

* In case of composition, the inner object ceases to exist when the object containing it ceases to exist. The objects are tightly coupled. For instance, song will not exist without the artist.
* Composition is implemented by creating the required objects inside the outer object during its initialization.

## Aggregation

* In case of aggregation, the objects are loosely coupled. The inner object continues to exist, even if the object containing it gets deleted.

* For instance, relationship between a playlist and a song. A song can still exist even if the playlist gets deleted.

* **Logical grouping scenarios are good examples of aggregation**. Suppose we have items and we wanted to group items, the relationship between item and item group is aggregation.

## Generalization and Specialization (Inheritance)

* Achieved using inheritance. Often this form of relation is described using **is a** phrase.
