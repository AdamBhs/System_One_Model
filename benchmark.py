import ollama
import time

tests = [
    # Difficult market-related questions: expected true
    "Why did NVIDIA fall 8% today despite reporting record revenue?",
    "If I invested $1,000 in Apple five years ago, what would it be worth now?",
    "Is Tesla expensive at its current valuation compared with its earnings?",
    "What happened to tech stocks after the Federal Reserve announcement?",
    "MSFT is up 3.2%, but its trading volume is down 20%. What could that mean?",
    "My portfolio lost value today. Could rising interest rates explain it?",
    "Which performed better this quarter, Amazon shares or Google's?",
    "Could Meta's latest earnings explain its falling share price?",

    # Difficult unrelated questions: expected false
    "The market was crowded when I went shopping for groceries.",
    "My dog loves eating chicken. Should I buy him more expensive food?",
    "I got a 20% discount on a laptop that originally cost $1,000.",
    "How do I sort stock symbols alphabetically using Python?",
    "My friend says I'm investing too much time in video games. Is he right?",
    "The stock pot is boiling. Should I lower the temperature?",
    "I improved my performance at work by 10%.",
    "I bought a Tesla toy car for $50. Was it worth the price?",

    # Ambiguous questions
    "What is the market doing today?",
    "Is Apple a good company?",
    "The price went up by 5%. What should I do?",
    "Can you explain what inflation means?",
]

total_start = time.perf_counter()
times = []

for i, question in enumerate(tests, start=1):
    start_time = time.perf_counter()

    try:
        response = ollama.systemone(
            model='tev1:0.8b',
            state=question,
            questions={
                'is_market_related': {
                    'type': 'noul',
                    'instructions': (
                        'Determine whether the text is related '
                        'to financial markets or investing.'
                    ),
                    'criteria': {
                        'true': (
                            'The text discusses stocks, stock prices, '
                            'trading, investments, portfolios, market '
                            'movements, company earnings as investments, '
                            'or financial market news.'
                        ),
                        'false': (
                            'The text is unrelated to financial markets '
                            'or investing. Incidental financial-sounding '
                            'words do not make it market-related. General '
                            'company questions without financial context '
                            'are false.'
                        ),
                    },
                },
            },
        )

        elapsed = time.perf_counter() - start_time
        times.append(elapsed)

        result = response.answers['is_market_related'].noul

        print(f"\n{i:02}. Question: {question}")
        print(f"    Classification: {result}")
        print(f"    Time: {elapsed:.3f} seconds")

    except Exception as e:
        print(f"\n{i:02}. Question: {question}")
        print(f"    ERROR: {e}")

    print("-" * 80)

total_elapsed = time.perf_counter() - total_start

print("\n========== BENCHMARK RESULTS ==========")
print(f"Questions: {len(tests)}")
print(f"Successful requests: {len(times)}")
print(f"Total time: {total_elapsed:.2f} seconds")

if times:
    print(f"Average time: {sum(times) / len(times):.3f} seconds")
    print(f"Fastest: {min(times):.3f} seconds")
    print(f"Slowest: {max(times):.3f} seconds")

print("=======================================")