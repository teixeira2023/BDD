# features/dictionary.feature

Feature: Pass a dictionary to Python

    Scenario: Pass a dictionary as JSON
        Given the following dictionary as JSON:
            """
            {
                "light_state": "on",
                "feature_state": "enabled"
            }
            """
        Then the dictionary should be correctly passed in json format
