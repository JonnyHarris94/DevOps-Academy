from todo_app.data.trello_items import Card, ViewModel

class Testcard:

    @staticmethod
    def test_to_do_items():

        #arrange
        card1 = Card("id","60c73323b5d71d7a754a20fc","title")
        card2 = Card("id2","status2","title2")
        view_model = ViewModel([card1,card2])
        #act
        result = view_model.todoitems

        #assert
        assert result == [card1]






    
    
        
