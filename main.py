def main():
    print("Hello from test!")


if __name__ == "__main__":
    main()
import seaborn as sns
df = sns.load_dataset("penguins")
print(df.head())
