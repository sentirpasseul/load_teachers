import pandas as pd

teachers = ["Евдокимова И. С.", "Глушкова И. И.", "Найханова Л. В.", "Жамбалов Э. Б.",
            "Ситниченко А. С.", "Бильгаева Н. Ц."
            ]

dolg = ["доцент", "преподаватель", "профессор", "преподаватель", "преподаватель", "доцент"]
stavka = [1,1,0.75,1,0.5,0.5]
zan_clock1 = [100, 85,65,97,50,50]
zan_clock2 = [110, 90, 50, 89, 48, 55]

data = pd.DataFrame({"fio": teachers, "dolg":dolg, "stavka":stavka, "zan_clock1": zan_clock1, "zan_clock2": zan_clock2})

