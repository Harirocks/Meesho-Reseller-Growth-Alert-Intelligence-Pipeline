from part2_engine.growth_engine import mom_growth, is_flagged, validate_feed


def test_april_to_may_ethnic_wear():
    # Given
    previous = 104520.77
    current = 185107.61

    # When
    growth = mom_growth(previous, current)
    result = is_flagged(growth)

    # Then
    assert growth == 77.1
    assert result == "flagged"

def test_may_to_june_beauty_personal_care():
    # Given
    previous = 35542.11
    current = 37559.07

    # When
    growth = mom_growth(previous, current)
    result = is_flagged(growth)

    # Then
    assert growth == 5.67
    assert result == "not_flagged"

def test_exact_boundary_escalation():
    # Given
    previous = 100000
    current = 108000

    # When
    growth = mom_growth(previous, current)
    result = is_flagged(growth)

    # Then
    assert growth == 8.0
    assert result == "escalate_exact_boundary"

def test_corrupted_feed():
    # Given
    csv_path = "part2_engine/fixtures/corrupted_feed.csv"

    # When
    valid, errors = validate_feed(csv_path)

    # Then
    assert valid is False
    assert len(errors) == 3

    assert errors == [
        "line 3: negative revenue (-4200.0) for category=Western Wear",
        "line 4: missing category (month=July)",
        "line 6: missing revenue (category=Home & Kitchen)",
    ]