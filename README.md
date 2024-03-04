# 🎓 `degree-classifier`

> **Note:**
This is a super quick personal tool to calculate some insights associated with BSC degree classification, based on data provided in a `CSV` file.

## Idea 🧠

The project allows you to calculate the following insights associated with your degree:
- List of all module marks (up-to-date).
- Averages on a year-by-year basis.
- Total (or current) degree average, assuming that `Y2` and `Y3` count as `33.3%` and `66.7%` respectively.

## Running the App 🚀

Follow these steps to get `degree-classifier` up and running on your machine:

1. **Check Python and Pip Installation:**
   Ensure you have `python3` and `pip` installed. You can verify their installation by running the following commands in your terminal:

   ```shell
   python3 -V
   pip -V
   ```

   > **Warning:**
   If your shell fails to recognize these commands, please install `Python` and `Pip` from their official sites: [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/).

2. **Repo Clone:**
   Clone the repository from `GitHub`:

   ```shell
   git clone https://github.com/chizo4/degree-classifier.git
   ```

3. **Setup:**
   Navigate to the root directory of the project and run the setup script (it initializes the data file in a specified path):

   ```shell
   cd degree-classifier
   bash setup.sh
   ```
  
5. **Run the `main` Program:**
   To make use of this project and find insights associated with your grades, please execute the following commands (make sure you are in the root of the repo):

   ```shell
   cd code
   python main.py
   ```

   Done with that, you can see further instructions about what can be calculated, and so on.

   > **Adding Your Grades:**
   You can add your grades into the CSV file by using the `i` option provided in the very silly CLI that I created, or by adding them directly into the CSV file. If going with the latter, you can refer to [this](https://github.com/chizo4/degree-classifier/blob/main/data/template.csv) file to find an example. 

## Contribution & Collaboration 🤝

> **Note:**
This is a very quick project with a small scope, but in case you find a mistake or had an idea on how to improve it, feel free to contact me via any of the links included in my [GitHub bio page](https://github.com/chizo4). Or, you might also contribute to the project by opening a [Pull Request](https://github.com/chizo4/degree-classifier/pulls) with suggested improvements.