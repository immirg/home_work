import pytest

from .homework_16_1 import TeamLead


class TestTeamLead:

    @pytest.mark.parametrize('value', ['departament', 'programming_language', 'team_size', 'salary'])
    def test_check_attributes_in_team_lead(self, value):
        team_lead = TeamLead(name='Alan', team_size=7, departament='AQA', programming_language='Python', salary=4000)
        assert hasattr(team_lead, value), f'Атрибут \'{value}\' отсуствует у объекта TeamLead'
