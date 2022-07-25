"""main"""
def main():
    """input grade"""
    grade = float(input())
    if grade < 1.00:
        print("I'm so sad.")
    elif 1 <= grade < 2.00:
        print("%.2f"% (2 - grade + 2))
    elif grade >= 2.00:
        print("I'm so happy.")
main()
