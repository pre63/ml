## The Little Proofer
_A tale of mathematical proofs_

### Chapter 1: What is a Proof?

#### 1.1: Definition
**Question:** What is a proof?

**Answer:** A proof is a logical argument that demonstrates the truth of a mathematical statement.

#### 1.2: Components
**Question:** What are the components of a proof?

**Answer:** The components of a proof are assumptions, logical deductions, and conclusions.

#### 1.3: Example
**Question:** Can you give me an example?

**Answer:** Sure. Let's prove that the sum of two even numbers is even.

#### 1.4: Assumptions
**Question:** What are our assumptions?

**Answer:** We assume that we have two even numbers, say $a$ and $b$.

**Question:** What does it mean for a number to be even?

**Answer:** A number is even if it can be written as $2k$ for some integer $k$.

#### 1.5: Logical Deductions
**Question:** How do we write $a$ and $b$ if they are even?

**Answer:** We write $a = 2k$ and $b = 2m$ for some integers $k$ and $m$.

**Question:** What happens when we add $a$ and $b$?

**Answer:** We get $a + b = 2k + 2m$.

**Question:** Can we factor $2k + 2m$?

**Answer:** Yes, $2k + 2m = 2(k + m)$.

#### 1.6: Conclusion
**Question:** What does $2(k + m)$ tell us about $a + b$?

**Answer:** It tells us that $a + b$ is even, because it is in the form of $2$ times an integer.

**Question:** What have we just done?

**Answer:** We have just completed a proof that the sum of two even numbers is even.

### Chapter 2: Direct Proofs

#### 2.1: Definition
**Question:** What is a direct proof?

**Answer:** A direct proof demonstrates the truth of a statement by straightforward logical deductions from the assumptions.

#### 2.2: Example
**Question:** Can you give me an example?

**Answer:** Sure. Let's prove that the square of an even number is even.

#### 2.3: Assumptions
**Question:** What is our assumption?

**Answer:** We assume that $n$ is an even number.

#### 2.4: Logical Deductions
**Question:** How do we write $n$ if it is even?

**Answer:** We write $n = 2k$ for some integer $k$.

**Question:** What happens when we square $n$?

**Answer:** We get $n^2 = (2k)^2 = 4k^2$.

**Question:** Can we factor $4k^2$?

**Answer:** Yes, $4k^2 = 2(2k^2)$.

#### 2.5: Conclusion
**Question:** What does $2(2k^2)$ tell us about $n^2$?

**Answer:** It tells us that $n^2$ is even, because it is in the form of $2$ times an integer.

**Question:** What have we just done?

**Answer:** We have just completed a direct proof that the square of an even number is even.

### Chapter 3: Proof by Contradiction

#### 3.1: Definition
**Question:** What is a proof by contradiction?

**Answer:** A proof by contradiction shows that a statement is true by assuming that it is false and then deriving a contradiction.

#### 3.2: Example
**Question:** Can you give me an example?

**Answer:** Sure. Let's prove that $\sqrt{2}$ is irrational.

#### 3.3: Assumptions
**Question:** What is our assumption?

**Answer:** We assume that $\sqrt{2}$ is rational.

**Question:** What does it mean for $\sqrt{2}$ to be rational?

**Answer:** It means that $\sqrt{2} = \frac{a}{b}$ for some integers $a$ and $b$ with no common factors other than 1.

#### 3.4: Logical Deductions
**Question:** What happens when we square both sides of $\sqrt{2} = \frac{a}{b}$?

**Answer:** We get $ 2 = \frac{a^2}{b^2}$.

**Question:** How can we rewrite this equation?

**Answer:** We rewrite it as $2b^2 = a^2$.

**Question:** What does $2b^2 = a^2$ tell us about $a$?

**Answer:** It tells us that $a^2$ is even, and thus $a$ must be even.

**Question:** If $a$ is even, how can we write $a$?

**Answer:** We write $a = 2k$ for some integer $k$.

**Question:** What happens when we substitute $a = 2k$ into $2b^2 = a^2$?

**Answer:** We get $2b^2 = (2k)^2 = 4k^2$.

**Question:** Can we simplify $2b^2 = 4k^2$?

**Answer:** Yes, we get $b^2 = 2k^2$.

**Question:** What does $b^2 = 2k^2$ tell us about $b$?

**Answer:** It tells us that $b^2$ is even, and thus $b$ must be even.

#### 3.5: Contradiction
**Question:** What have we shown about $a$ and $b$?

**Answer:** We have shown that both $a$ and $b$ are even.

**Question:** What does this imply about $\frac{a}{b}$?

**Answer:** It implies that $\frac{a}{b}$ is not in its simplest form, contradicting our assumption.

**Question:** What can we conclude from this contradiction?

**Answer:** We conclude that $\sqrt{2}$ is irrational.

**Question:** What have we just done?

**Answer:** We have just completed a proof by contradiction that $\sqrt{2}$ is irrational.

### Chapter 4: Proof by Induction

#### 4.1: Definition
**Question:** What is a proof by induction?

**Answer:** A proof by induction shows that a statement is true for all natural numbers by proving it for the first number and assuming it for $n$ to prove it for $n + 1$.

#### 4.2: Example
**Question:** Can you give me an example?

**Answer:** Sure. Let's prove that the sum of the first $n$ natural numbers is $\frac{n(n+1)}{2}$.

#### 4.3: Base Case
**Question:** What is the base case?

**Answer:** The base case is $n = 1$.

**Question:** What is the sum of the first natural number?

**Answer:** The sum is $1$.

**Question:** Does $1$ equal $\frac{1(1+1)}{2}$?

**Answer:** Yes, $1 = \frac{1 \cdot 2}{2}$.

#### 4.4: Inductive Step
**Question:** What is the inductive step?

**Answer:** We assume the statement is true for $n$ and prove it for $n + 1$.

#### 4.5: Assumption
**Question:** What is our assumption?

**Answer:** We assume that the sum of the first $n$ natural numbers is $\frac{n(n+1)}{2}$.

#### 4.6: Logical Deductions
**Question:** What happens when we add $n + 1$ to the sum of the first $n$ natural numbers?

**Answer:** We get $\frac{n(n+1)}{2} + (n + 1)$.

**Question:** How can we simplify $\frac{n(n+1)}{2} + (n + 1)$?

**Answer:** We can factor out $n + 1$, getting $\frac{n(n+1) + 2(n+1)}{2}$.

**Question:** What does this simplify to?

**Answer:** This simplifies to $\frac{(n+1)(n+2)}{2}$.

#### 4.7: Conclusion
**Question:** What does $\frac{(n+1)(n+2)}{2}$tell us about the sum of the first $n + 1$ natural numbers?

**Answer:** It tells us that the sum of the first $n + 1$ natural numbers is $\frac{(n+1)(n+2)}{2}$, which matches our formula.

**Question:** What have we just done?

**Answer:** We have just completed a proof by induction that the sum of the first $n$ natural numbers is $\frac{n(n+1)}{2}$.

### Chapter 5: Proof by Contr

apositive

#### 5.1: Definition
**Question:** What is a proof by contrapositive?

**Answer:** A proof by contrapositive shows that a statement is true by proving that its contrapositive is true.

#### 5.2: Example
**Question:** Can you give me an example?

**Answer:** Sure. Let's prove that if $n^2$ is even, then $n$ is even.

#### 5.3: Contrapositive
**Question:** What is the contrapositive of the statement?

**Answer:** The contrapositive is if $n$ is odd, then $n^2$ is odd.

#### 5.4: Assumption
**Question:** What is our assumption?

**Answer:** We assume that $n$ is odd.

**Question:** What does it mean for $n$ to be odd?

**Answer:** It means that $n = 2k + 1$ for some integer $k$.

#### 5.5: Logical Deductions
**Question:** What happens when we square $n$?

**Answer:** We get $n^2 = (2k + 1)^2 = 4k^2 + 4k + 1$.

**Question:** Can we factor $4k^2 + 4k + 1$?

**Answer:** Yes, $4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$.

#### 5.6: Conclusion
**Question:** What does $2(2k^2 + 2k) + 1$ tell us about $n^2$?

**Answer:** It tells us that $n^2$ is odd, because it is in the form of $2$ times an integer plus 1.

**Question:** What have we just done?

**Answer:** We have just completed a proof by contrapositive that if $n^2$ is even, then $n$ is even.

### Chapter 6: Proof by Cases

#### 6.1: Definition
**Question:** What is a proof by cases?

**Answer:** A proof by cases shows that a statement is true by dividing it into several cases and proving each one separately.

#### 6.2: Example
**Question:** Can you give me an example?

**Answer:** Sure. Let's prove that $|a+b| \leq |a| + |b|$.

#### 6.3: Cases
**Question:** What are our cases?

**Answer:** Our cases are whether $a$ and $b$ are positive, negative, or zero.

#### 6.4: Case 1
**Question:** What is case 1?

**Answer:** Case 1 is when $a \geq 0$ and $b \geq 0$.

**Question:** What happens in this case?

**Answer:** $|a+b| = a + b$ and $|a| + |b| = a + b$.

**Question:** Is $|a+b| \leq |a| + |b|$ true in this case?

**Answer:** Yes, because $a + b = a + b$.

#### 6.5: Case 2
**Question:** What is case 2?

**Answer:** Case 2 is when $a \geq 0$ and $b < 0$.

**Question:** What happens in this case?

**Answer:** $|a+b| \leq a + |b|$.

**Question:** Why is this true?

**Answer:** Because $|b| = -b$ when $b < 0$, so $|a+b| = a - b \leq a + (-b) = a + |b|$.

#### 6.6: Case 3
**Question:** What is case 3?

**Answer:** Case 3 is when $a < 0$ and $b \geq 0$.

**Question:** What happens in this case?

**Answer:** $|a+b| \leq |a| + b$.

**Question:** Why is this true?

**Answer:** Because $|a| = -a$ when $a < 0$, so $|a+b| = -a + b \leq (-a) + b = |a| + b$.

#### 6.7: Case 4
**Question:** What is case 4?

**Answer:** Case 4 is when $a < 0$ and $b < 0$.

**Question:** What happens in this case?

**Answer:** $|a+b| \leq |a| + |b|$.

**Question:** Why is this true?

**Answer:** Because both $a$ and $b$ are negative, $|a+b| = -(a+b) = -a - b = |a| + |b|$.

#### 6.8: Conclusion
**Question:** What have we just done?

**Answer:** We have completed a proof by cases that $|a+b| \leq |a| + |b|$.

### Conclusion
This concludes our exploration of different proof techniques. We've covered direct proofs, proofs by contradiction, proofs by induction, proofs by contrapositive, and proofs by cases. Each method helps us rigorously establish the truth of mathematical statements. Practice these techniques to become proficient in crafting clear, logical, and convincing proofs.