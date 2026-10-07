"""Stage 3 - add school-level mathematical foundations to 2.11.

The Math & Theoretical CS section began at university level (linear algebra,
calculus), leaving no route in for someone who needs algebra, functions,
exponents and logarithms first. This topic fills that gap for every
technical path in the map (first used by the Gen AI & LLMs derived map).
Approved by the repo owner on 2026-10-07.
"""
import sys
sys.path.insert(0, "scripts")
import _mapkit as mk

data = mk.load()
r = mk.root(data)

SUBS = [
 ("Numbers & Arithmetic", [
  "What numbers are and why they matter", "Whole numbers, integers and the number line",
  "The four operations and their properties", "Order of operations",
  "Negative numbers and signed arithmetic", "Factors, multiples and primes",
  "Divisibility and remainders", "Rounding and estimation",
  "Mental arithmetic strategies", "Scientific notation for very large and small numbers",
  "Precision, significant figures and error", "Arithmetic as the base of all computation"]),
 ("Fractions, Ratios & Percentages", [
  "What a fraction represents", "Equivalent fractions and simplifying",
  "Adding and subtracting fractions", "Multiplying and dividing fractions",
  "Decimals and their link to fractions", "Ratios and proportions",
  "Rates and unit rates", "Percentages and percentage change",
  "Percentage points versus percent", "Averages: mean, median and mode",
  "Proportional reasoning in everyday decisions", "Ratios and percentages in technical work"]),
 ("Algebraic Expressions", [
  "Why letters stand for numbers", "Variables, constants and coefficients",
  "Writing expressions from words", "Simplifying and collecting like terms",
  "Expanding brackets", "Factorising expressions",
  "Substituting values into expressions", "Formulas and rearranging them",
  "Indices notation inside expressions", "Common algebraic mistakes",
  "Reading mathematical notation fluently", "Algebra as the language of models"]),
 ("Equations & Inequalities", [
  "What an equation says", "Solving linear equations step by step",
  "Equations with variables on both sides", "Simultaneous equations",
  "Quadratic equations and their solutions", "Completing the square and the formula",
  "Inequalities and how they differ from equations", "Solving and graphing inequalities",
  "Absolute value", "Checking solutions",
  "Word problems into equations", "Equations as constraints in optimisation"]),
 ("Functions & Their Graphs", [
  "What a function is", "Inputs, outputs, domain and range",
  "Function notation", "Plotting points and reading graphs",
  "The coordinate plane", "Composing functions",
  "Inverse functions", "Increasing, decreasing and turning points",
  "Piecewise functions", "Transformations of graphs",
  "Functions with several inputs", "Functions as the core idea of machine learning"]),
 ("Linear & Polynomial Functions", [
  "Straight lines and the equation y = mx + c", "Slope as a rate of change",
  "Intercepts and their meaning", "Fitting a line to data by eye",
  "Parallel and perpendicular lines", "Quadratic functions and parabolas",
  "Polynomials of higher degree", "Roots and factors of polynomials",
  "Growth of polynomial functions", "Linear models in practice",
  "When straight lines fail", "From linear functions to linear algebra"]),
 ("Exponents & Exponential Functions", [
  "Powers and repeated multiplication", "Laws of exponents",
  "Zero, negative and fractional exponents", "Square roots and other roots",
  "Exponential growth", "Exponential decay",
  "Compound interest as an exponential process", "The number e",
  "Doubling time and half-life", "Exponential versus polynomial growth",
  "Exponentials in technology trends", "The exponential function in neural networks"]),
 ("Logarithms", [
  "What a logarithm asks", "Logarithms as inverses of exponentials",
  "Laws of logarithms", "Common, natural and binary logarithms",
  "Changing the base", "Solving exponential equations with logarithms",
  "Logarithmic scales", "Orders of magnitude",
  "Logarithms in measuring information", "Log-likelihood and log-probabilities",
  "Logarithms in algorithm analysis", "Reading log-scale charts correctly"]),
 ("Sequences, Series & Summation", [
  "What a sequence is", "Arithmetic sequences",
  "Geometric sequences", "Sigma notation for sums",
  "Arithmetic and geometric series", "Infinite series and convergence",
  "Products and pi notation", "Recursive definitions",
  "Averages written as sums", "Sums over data sets",
  "Indices and subscripts in formulas", "Summation in machine-learning formulas"]),
 ("Sets, Logic & Mathematical Notation", [
  "Sets and elements", "Union, intersection and complement",
  "Venn diagrams", "Number sets and intervals",
  "Logical statements and connectives", "If-then statements and implication",
  "Quantifiers: for all and there exists", "Reading Greek letters and symbols",
  "Common notation in technical papers", "Definitions, theorems and proofs",
  "Precision in mathematical language", "From notation to understanding"]),
 ("Geometry, Trigonometry & Coordinates", [
  "Points, lines, angles and shapes", "Distance and Pythagoras' theorem",
  "Coordinates in two and three dimensions", "Perimeter, area and volume",
  "Similarity and scale", "Sine, cosine and tangent",
  "Radians and the unit circle", "Trigonometric graphs and waves",
  "Vectors as arrows", "Angles between directions",
  "Distance and similarity between points", "Geometry in high-dimensional spaces"]),
 ("Bridging to University Mathematics for AI", [
  "Why AI needs mathematics", "From functions to models",
  "From slopes to derivatives", "From arrows to vectors and matrices",
  "From counting to probability", "From averages to statistics",
  "From logarithms to entropy and loss", "Reading an equation in a research paper",
  "Building mathematical confidence", "Practising mathematics effectively",
  "Using software and AI tools for mathematics", "A roadmap from school maths to ML maths"]),
]

log = ["ADD TOPIC " + mk.add_topic(
    r, "2.11. ", "2.11.13",
    "Mathematical Foundations: Algebra, Functions, Exponents & Logarithms", SUBS)]

mk.save(data)
print("\n".join(log))
