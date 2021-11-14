import re


class Node:
    """Объект класса Node обрабатывает запись о пользователе.
    :parameter
    node:dict
    """
    node: dict

    def __init__(self, _node):
        self.node = _node.copy()

    def check_telephone(self) -> bool:
        pattern = "^\\+7-\\(\\d{3}\\)-\\d{3}(-\\d{2}){2}"
        if re.match(pattern, self.node["telephone"]):
            return True
        return False

    def check_weight(self) -> bool:
        pattern = "^([1-9]|[1-9][0-9]|1[0-9][1-9]|2[0-5][0-9])$"
        if re.match(pattern, str(self.node["weight"])):
            return True
        return False

    def check_inn(self) -> bool:
        pattern = "^[0-9]{12}$"
        if re.match(pattern, self.node["inn"]):
            return True
        return False

    def check_passport_series(self) -> bool:
        pattern = "\\d{2} \\d{2}"
        if re.match(pattern, self.node["passport_series"]):
            return True
        return False

    def check_university(self) -> bool:
        pattern = "^.*(?:СПбГУ|МФТИ|МГУ|МГТУ|им\\.|[Уу]нивер|[Аа]кадем|[Ии]нстит|[Нн]ационал).*$"
        if re.match(pattern, self.node["university"]):
            return True
        return False

    def check_work_experience(self) -> bool:
        pattern = "^([1-9]|[1-6][0-9])$"
        if re.match(pattern, str(self.node["work_experience"])):
            return True
        return False

    def check_academic_degree(self) -> bool:
        pattern = "Доктор наук|Магистр|Кандидат наук|Специалист|Бакалавр"
        if re.match(pattern, self.node["academic_degree"]):
            return True
        return False

    def check_worldview(self) -> bool:
        pattern = "^.+(?:изм|ство|ам)$"
        if re.match(pattern, self.node["worldview"]):
            return True
        return False

    def check_address(self) -> bool:
        pattern = "^[\\wа-яА-Я\\s\\.\\d-]* \\d+$"
        if re.match(pattern, self.node["address"]):
            return True
        return False
