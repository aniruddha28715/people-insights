import unittest
from people_insights import PeopleInsightsGenerator

class TestPeopleInsights(unittest.TestCase):
    def setUp(self):
        self.generator = PeopleInsightsGenerator()
        self.sample_employee = {
            "name": "Test User",
            "email": "test@company.com",
            "role": "Software Engineer",
            "performance_metrics": {
                "productivity": 85,
                "teamwork": 90,
                "communication": 88
            },
            "recent_achievements": [
                "Test achievement 1",
                "Test achievement 2"
            ]
        }

    def test_generate_insights(self):
        """Test insights generation"""
        insights = self.generator.generate_insights(self.sample_employee, "Test Manager")
        self.assertIsNotNone(insights)
        self.assertIn(self.sample_employee["name"], insights)
        self.assertIn("Test Manager", insights)

    def test_performance_thresholds(self):
        """Test performance threshold recommendations"""
        # Test low productivity
        self.sample_employee["performance_metrics"]["productivity"] = 75
        insights = self.generator.generate_insights(self.sample_employee, "Test Manager")
        self.assertIn("productivity improvement", insights.lower())

        # Test low teamwork
        self.sample_employee["performance_metrics"]["teamwork"] = 80
        insights = self.generator.generate_insights(self.sample_employee, "Test Manager")
        self.assertIn("team collaboration", insights.lower())

    def test_achievements_inclusion(self):
        """Test that achievements are included in insights"""
        insights = self.generator.generate_insights(self.sample_employee, "Test Manager")
        for achievement in self.sample_employee["recent_achievements"]:
            self.assertIn(achievement, insights)

if __name__ == '__main__':
    unittest.main() 