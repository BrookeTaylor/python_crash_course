"""

    Title: 
    Author: Eric Matthes
    Date: 04/28/2023
    Description: "In test_survey.py (in the pass folder), we created a new 
    instance of AnonymousSurvey in each test function. This is fine in the 
    short example we're working with, but in a real-world project with tens or 
    hundreds of tests, this would be problematic. 
    
    In testing, a fixture helps set up a test environment. Often, this means 
    creating a resource that's used by more than one test. We create a fixture 
    in pytest by writing a function with the decorator @pytest.fixture. A 
    decorator is a directive placed just before a function definition; Python 
    applies this directive to the function before it runs, to alter how the 
    function code behaves. Don't worry if this sounds complicated; you can 
    start to use decorators from third-party packages before learning to write 
    them yourself. 
    
    Let's use a fixture to create a single survey instance that can be used in 
    both test functions in test_survey.py:
    
    We need to import pytest now, because we're using a decorator that's 
    defined in pytest. We apply the @pytest.fixture decorator to the new 
    function language_survey(). This function builds an AnonymousSurvey object 
    and returns the new survey."

"""

import pytest

from survey import AnonymousSurvey

@pytest.fixture


def language_survey():

    # A survey that will be available to all test functions.
    question = "What language did you first learn to speak?"

    language_survey = AnonymousSurvey(question)

    return language_survey


def test_store_single_response(language_survey):

    # Test that a single response is stored properly. 
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


def test_store_three_responses(language_survey):

    # Test that three individual responses are stored properly.
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses

