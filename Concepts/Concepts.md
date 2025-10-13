Ordinary Least Squares (OLS) estimates coefficients by **minimizing the sum of squared residuals** — that is, the total squared difference between the observed values (( y_i )) and the predicted values (( \hat{y}_i )) from the linear model.

Formally, OLS minimizes this quantity:

[
\text{SSE} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
]

where

* ( y_i ) = actual dependent variable value,
* ( \hat{y}*i = \beta_0 + \beta_1 x*{i1} + \beta_2 x_{i2} + \dots + \beta_k x_{ik} ) = predicted value from the model.

✅ **In short:** OLS minimizes the **Sum of Squared Errors (SSE)** (also known as the **Residual Sum of Squares, RSS**).

**Answer:**
Overfitting is most strongly suggested when you see **a high train R² and a much lower test R²**.

---

### **Explanation:**

In polynomial regression:

* **Train R² (training set performance)** measures how well the model fits the data it was trained on.
* **Test R² (testing set performance)** measures how well the model generalizes to unseen data.

When:

* The **train R² is very high** (close to 1), it means the model fits the training data almost perfectly.
* The **test R² is much lower** (or even negative), it means the model performs poorly on new data.

This gap indicates that the model has **learned the noise and random fluctuations** in the training data rather than the true underlying pattern — the classic symptom of **overfitting**.

---

### **In short:**

* **High train R²:** Model memorized the training data.
* **Low test R²:** Model fails to generalize to unseen data.
  ➡️ **Conclusion:** The model is **overfitted**.

**Answer:**
✅ **Root Mean Squared Error (RMSE)** is in the **same units** as the target variable.

---

### **Explanation:**

RMSE is defined as:

[
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
]

Here’s why it has the **same units as the target variable ((y))**:

1. **Inside the formula**, we compute the squared difference ((y_i - \hat{y}_i)^2).

   * This squaring step changes the units to “target²” (e.g., if target is dollars, units become dollars²).

2. **Taking the square root** at the end reverses that squaring.

   * The result goes back to the original units of the target variable (e.g., dollars).

---

### **Why this matters:**

Because RMSE is in the same units as the target, it’s **intuitively interpretable** — you can directly say,

> “On average, the model’s predictions are off by about **X units** of the target.”

For example:
If the target is **house price in $**, and RMSE = **25,000**,
→ it means the model’s typical prediction error is **$25,000**.


