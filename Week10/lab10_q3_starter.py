# ============================================================
#  WEEK 10 LAB — Q3: SECURITY AUDIT LOG + UNIT TESTS
#  COMP2152 — [Omar Butt]
# ============================================================

import sqlite3
import unittest

DB_NAME = "audit.db"

# --- Helpers (provided) ---
def seed_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS audit_log")
    cursor.execute("""CREATE TABLE audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        user TEXT,
        action TEXT,
        severity TEXT,
        details TEXT
    )""")

    sample_data = [
        ("2026-03-16 08:00:00", "admin", "LOGIN", "LOW", "Successful login"),
        ("2026-03-16 08:05:00", "root", "FAILED_LOGIN", "HIGH", "Failed SSH"),
        ("2026-03-16 08:10:00", "admin", "FILE_ACCESS", "LOW", "Read config"),
        ("2026-03-16 08:15:00", "root", "FAILED_LOGIN", "HIGH", "Failed SSH"),
        ("2026-03-16 08:20:00", "guest", "FILE_MODIFY", "MEDIUM", "Modified file"),
        ("2026-03-16 08:25:00", "admin", "PERMISSION_CHANGE", "HIGH", "Changed perms"),
        ("2026-03-16 08:30:00", "guest", "LOGOUT", "LOW", "Session ended"),
        ("2026-03-16 08:35:00", "backup", "FILE_ACCESS", "LOW", "Read backup"),
        ("2026-03-16 08:40:00", "guest", "FILE_MODIFY", "MEDIUM", "Modified file"),
        ("2026-03-16 08:45:00", "admin", "LOGOUT", "LOW", "Session ended"),
    ]

    cursor.executemany(
        "INSERT INTO audit_log (timestamp, user, action, severity, details) VALUES (?, ?, ?, ?, ?)",
        sample_data
    )

    conn.commit()
    conn.close()


# TODo: Complete
def get_events_by_severity(severity):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM audit_log WHERE severity = ?", (severity,))
    rows = cursor.fetchall()

    conn.close()
    return rows


def get_recent_events(limit):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM audit_log ORDER BY timestamp DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()

    conn.close()
    return rows


def count_by_severity():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT severity, COUNT(*) FROM audit_log GROUP BY severity ORDER BY COUNT(*) DESC"
    )
    rows = cursor.fetchall()

    conn.close()
    return rows


def safe_query(query):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()


# --- UNIT TESTS ---
class TestAuditLog(unittest.TestCase):

    def setUp(self):
        seed_database()

    def test_high_severity(self):
        events = get_events_by_severity("HIGH")
        self.assertEqual(len(events), 3)

    def test_recent_events(self):
        events = get_recent_events(5)
        self.assertEqual(len(events), 5)

    def test_count(self):
        counts = count_by_severity()
        self.assertIn(("HIGH", 3), counts)

    def test_safe_bad_query(self):
        result = safe_query("SELECT * FROM fake_table")
        self.assertEqual(result, [])


# --- Main ---
if __name__ == "__main__":
    print("\n--- Running Unit Tests ---")
    unittest.main(verbosity=2)