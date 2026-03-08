import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import check_guess, update_score, parse_guess


# --- Bug 1: Backwards hint messages ---
# Before the fix, "Too High" returned "📈 Go HIGHER!" and "Too Low" returned "📉 Go LOWER!"

def test_too_high_returns_go_lower():
    """When guess > secret the message must say Go LOWER, not Go HIGHER."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message but got: {message!r}"

def test_too_low_returns_go_higher():
    """When guess < secret the message must say Go HIGHER, not Go LOWER."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message but got: {message!r}"

def test_win_returns_correct_message():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message or "🎉" in message


# --- Bug 2: Secret type alternating between int and str ---
# Before the fix, even-numbered attempts cast the secret to str,
# breaking numeric comparison (e.g. check_guess(50, "50") behaved incorrectly).

def test_check_guess_always_compares_as_int():
    """check_guess(guess_int, secret_int) must work regardless of call count."""
    for _ in range(4):  # simulate several attempts
        outcome, _ = check_guess(75, 50)
        assert outcome == "Too High"

def test_check_guess_win_with_int_secret():
    """Winning when secret is kept as int (not converted to str on even attempts)."""
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


# --- Bug 3: Attempts counter initialised to 1 instead of 0 ---
# update_score receives attempt_number; with the old bug attempt_number started
# at 1 on the very first guess, so the win bonus was miscalculated.

def test_update_score_first_attempt_win():
    """Winning on the first attempt (attempt_number=0) should award max points."""
    # points = 100 - 10 * (0 + 1) = 90
    new_score = update_score(0, "Win", attempt_number=0)
    assert new_score == 90, f"Expected 90 but got {new_score}"

def test_update_score_would_have_been_wrong_with_old_init():
    """With the old bug attempts started at 1, giving 80 instead of 90 on first win."""
    wrong_score = update_score(0, "Win", attempt_number=1)  # old buggy value
    correct_score = update_score(0, "Win", attempt_number=0)
    assert correct_score > wrong_score


# --- Bug 4: Attempts incremented before guess was processed ---
# Before the fix, attempts was bumped at the top of the submit block so
# update_score always received attempt_number+1 relative to the actual attempt.

def test_update_score_attempt_zero_not_one():
    """First guess should use attempt_number=0, yielding 90 points on a win."""
    score = update_score(0, "Win", 0)
    assert score == 90

def test_update_score_attempt_nine_floors_at_10():
    """Points floor at 10 for late attempts."""
    score = update_score(0, "Win", 9)
    assert score == 10

def test_update_score_increments_accumulate():
    """Score accumulates correctly across multiple attempts when counter is right."""
    score = 0
    score = update_score(score, "Too Low", 0)   # -5
    score = update_score(score, "Too High", 1)  # -5
    score = update_score(score, "Win", 2)       # 100 - 10*3 = 70
    assert score == 60


# --- Existing core logic (kept for regression) ---

def test_parse_guess_valid():
    ok, val, err = parse_guess("42")
    assert ok is True
    assert val == 42
    assert err is None

def test_parse_guess_empty():
    ok, val, err = parse_guess("")
    assert ok is False

def test_parse_guess_non_number():
    ok, val, err = parse_guess("abc")
    assert ok is False
    assert "not a number" in err.lower()
