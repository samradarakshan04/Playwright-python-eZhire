Feature: Login

  Scenario Outline: Successful login
    Given the user is on the login page
    When the user logs in with "<username>" and "<password>"
    Then the user should see the dashboard

    Examples:
      | username  | password     |
      | tomsmith  | SuperSecretPassword  |
