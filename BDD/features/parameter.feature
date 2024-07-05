Feature: Set the feature enable when the user changes the gear position out of Park

    Scenario: Enable the feature when the user changes the gear position out of Park
        Given the cabin light state is 'on'
        And the gear is in 'Park'
        When the user changes the gear position out of 'Park'
        Then the cabin light state should be 'off'
