Feature: Cab As Office Light # features/lightOn.feature:1
    Scenario Outline: Dimming the light by holding the Hard Button # features/dimming.feature:1

        Feature The cab as office feature shall progressively dim the light  while the user presses the cab as office hard button to a minimum of 10%.
        Given the current cabin light is "<stateCabinLight>" # steps/validation.py:1
        And the cab as office hard button is "pressed"
        And the value of dimming is "<valueDimming>"
        And the light control menu is "displayed"
        And the hold timer is "<validTimeHold>" seconds
        When the driver "releases" the cabin as office hard button
        Then the cab as Office Light feature should set the luminosity to "<valueDimming_new>" %

        Examples:
            | stateCabinLight | valueDimming | valueDimming_new | validTimeHold |
            | on              | 100          | 20               | 4             |
            | on              | 90           | 20               | 3.5           |
            | on              | 80           | 20               | 3             |
            | on              | 70           | 20               | 2.5           |
            | on              | 60           | 20               | 2             |
            | on              | 50           | 20               | 1.5           |
            | on              | 40           | 20               | 1             |
            | on              | 30           | 20               | 0.5           |
            | on              | 50           | 10               | 4             |
