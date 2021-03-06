import pytest
from dsa.challenges.fifo_animal_shelter.fifo_animal_shelter import (
    Node,
    Dog,
    Cat,
    AnimalShelter,
    PseudoQueue
)

def test_AnimalShelter_enqueue_something():
    shelter = AnimalShelter()
    shelter.enqueue('something')
    actual = shelter.peek()
    expected = 'something'
    assert actual == expected

def test_AnimalShelter_enqueue_Dog():
    shelter = AnimalShelter()
    oliver = Dog('Oliver')
    shelter.enqueue(oliver)
    actual = shelter.peek()
    expected = oliver
    assert actual == expected

def test_AnimalShelter_enqueue_Cat():
    shelter = AnimalShelter()
    cheeto = Cat('Cheeto')
    oliver = Dog('Oliver')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.peek()
    expected = cheeto
    assert actual == expected

def test_AnimalShelter_dequeue_no_pref():
    shelter = AnimalShelter()
    cheeto = Cat('Cheeto')
    oliver = Dog('Oliver')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.dequeue()
    expected = None
    assert actual == expected

def test_AnimalShelter_dequeue_pref_not_catOrDog():
    shelter = AnimalShelter()
    cheeto = Cat('Cheeto')
    oliver = Dog('Oliver')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.dequeue('bird')
    expected = None
    assert actual == expected

def test_AnimalShelter_dequeue_pref_dog():
    shelter = AnimalShelter()
    cheeto = Cat('Cheeto')
    oliver = Dog('Oliver')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.dequeue('dog')
    expected = 'cat'
    assert actual == expected

def test_PseudoQueue_enqueue_cat():
    shelter = PseudoQueue()
    cheeto = Cat('Cheeto')
    oliver = Dog('Oliver')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.storage1.peek().kind
    expected = 'dog'
=======
    Dog,
    Cat,
    Bird,
    AnimalShelter
)

def test_AnimalShelter_enqueue_Dog():
    shelter = AnimalShelter()
    oliver = Dog('Oliver')
    shelter.enqueue(oliver)
    actual = str(shelter)
    expected = '[dog: Oliver] <- None'
    assert actual == expected

def test_AnimalShelter_enqueue_Dog_Cat():
    shelter = AnimalShelter()
    oliver = Dog('Oliver')
    cheeto = Cat('Cheeto')
    shelter.enqueue(oliver)
    shelter.enqueue(cheeto)
    actual = str(shelter)
    expected = '[dog: Oliver] <- [cat: Cheeto] <- None'
    assert actual == expected

def test_AnimalShelter_enqueue_Exception():
    with pytest.raises(Exception):
        shelter = AnimalShelter()
        cookie = Bird('Cookie')
        actual = shelter.enqueue(cookie)
        expected = 'We can only accept a cat or a dog.'
        assert actual == expected

def test_AnimalShelter_dequeue_dog_first():
    shelter = AnimalShelter()
    oliver = Dog('Oliver')
    cheeto = Cat('Cheeto')
    shelter.enqueue(oliver)
    shelter.enqueue(cheeto)
    actual = shelter.dequeque('dog')
    expected = 'Oliver'
    assert actual == expected

def test_AnimalShelter_dequeue_cat_first():
    shelter = AnimalShelter()
    oliver = Dog('Oliver')
    cheeto = Cat('Cheeto')
    shelter.enqueue(cheeto)
    shelter.enqueue(oliver)
    actual = shelter.dequeque('cat')
    expected = 'Cheeto'
    assert actual == expected

def test_AnimalShelter_dequeue_dog_not_first():
    shelter = AnimalShelter()
    oliver = Dog('Oliver')
    cheeto = Cat('Cheeto')
    sneakers = Cat('Sneakers')
    shelter.enqueue(cheeto)
    shelter.enqueue(sneakers)
    shelter.enqueue(oliver)
    actual = shelter.dequeque('dog')
    expected = 'Oliver'
    assert actual == expected

def test_AnimalShelter_dequeue_cat_not_first():
    shelter = AnimalShelter()
    oliver = Dog('Oliver')
    poncho = Dog('Poncho')
    cheeto = Cat('Cheeto')
    shelter.enqueue(oliver)
    shelter.enqueue(poncho)
    shelter.enqueue(cheeto)
    actual = shelter.dequeque('cat')
    expected = 'Cheeto'
    assert actual == expected

def test_AnimalShelter_dequeue_alternating():
    shelter = AnimalShelter()
    oliver = Dog('Oliver')
    cheeto = Cat('Cheeto')
    poncho = Dog('Poncho')
    sneakers = Cat('Sneakers')
    peso = Dog('Peso')
    shelter.enqueue(oliver)
    shelter.enqueue(poncho)
    shelter.enqueue(cheeto)
    shelter.enqueue(sneakers)
    shelter.enqueue(peso)
    actual = shelter.dequeque('cat')
    expected = 'Cheeto'

    assert actual == expected
