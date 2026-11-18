import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Extra Features | Regent Business School",
    page_icon="📈",
    layout="wide"
)

import streamlit as st
from sympy import symbols, Eq, solve

st.title("🧮 Solving Equations with Python")

x, y = symbols("x y")

# ---------------------------------
# Example 1: Linear Equation
# ---------------------------------

st.header("Example 1: Linear Equation")

st.latex(r"2x + 4x = 10")

st.subheader("Python Code")

st.code("""
from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(2*x + 4*x, 10)
answer = solve(equation, x)

print("Answer: x =", answer[0])
""", language="python")

equation = Eq(2*x + 4*x, 10)
answer = solve(equation, x)

st.subheader("Output")
st.write("Answer: x =", answer[0])
st.write("Decimal answer:", float(answer[0]))

st.divider()

# ---------------------------------
# Example 2: Quadratic Equation
# ---------------------------------

st.header("Example 2: Quadratic Equation")

st.latex(r"x^2 - 5x + 6 = 0")

st.subheader("Python Code")

st.code("""
from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(x**2 - 5*x + 6, 0)
answers = solve(equation, x)

print("First answer:", answers[0])
print("Second answer:", answers[1])
""", language="python")

equation = Eq(x**2 - 5*x + 6, 0)
answers = solve(equation, x)

st.subheader("Output")
st.write("First answer: x =", answers[0])
st.write("Second answer: x =", answers[1])

st.divider()

# ---------------------------------
# Example 3: Simultaneous Equations
# ---------------------------------

st.header("Example 3: Simultaneous Equations")

st.latex(r"2x + 3y = 12")
st.latex(r"x + y = 5")

st.subheader("Python Code")

st.code("""
from sympy import symbols, Eq, solve

x, y = symbols('x y')

equation1 = Eq(2*x + 3*y, 12)
equation2 = Eq(x + y, 5)

answers = solve((equation1, equation2), (x, y))

print("x =", answers[x])
print("y =", answers[y])
""", language="python")

equation1 = Eq(2*x + 3*y, 12)
equation2 = Eq(x + y, 5)

answers = solve((equation1, equation2), (x, y))

st.subheader("Output")
st.write("x =", answers[x])
st.write("y =", answers[y])

st.success("All equations solved successfully!")


