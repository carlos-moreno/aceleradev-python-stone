from main import classify_by_phone_number, records


class TestChallenge1:
    def test_len(self):
        result = classify_by_phone_number(records)
        assert len(result) == 6

    def test_result_default(self):
        result = classify_by_phone_number(records)
        expected_result = [
            {"source": "41-833333333", "total": 4.77},
            {"source": "48-999999999", "total": 4.68},
            {"source": "41-885633788", "total": 3.96},
            {"source": "48-996355555", "total": 2.61},
            {"source": "41-886383097", "total": 1.53},
            {"source": "48-996383697", "total": 1.35},
        ]
        assert result == expected_result
