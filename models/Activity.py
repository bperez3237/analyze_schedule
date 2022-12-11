

class Activity:
    def __init__(self, activity_status, area, activity_id, type, name, start_date, end_date, original_duration, remaining_duration, percent_complete, sub, category_1, category_2, cost_code, sub_cost_code):
        self.activity_status = activity_status
        self.area = area
        self.activity_id = activity_id
        self.type = type
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.original_duration = original_duration
        self.remaining_duration = remaining_duration
        self.percent_complete = percent_complete
        self.sub = sub
        self.category_1 = category_1
        self.category_2 = category_2
        self.cost_code = cost_code
        self.sub_cost_code = sub_cost_code

    def __str__(self):
        return f'Activity: {self.name}'