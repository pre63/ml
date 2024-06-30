# The Little Linear Algebra

## Chapter 1: Understanding Vectors

**What is a vector?**

> A vector is an object with both magnitude and direction.

**How do we write it?**

> $\vec{v} = \begin{pmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{pmatrix}$.

**What is the dimension of $\vec{v}$?**

> The number of components, $n$.

**What is $\vec{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ in 2D?**

> A vector with 3 units in the x-direction and 4 units in the y-direction.

Perfect!

## Chapter 2: Vector Operations

**How do we add vectors?**

> Component-wise. For $\vec{u} = \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}$ and $\vec{v} = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$,
   $\vec{u} + \vec{v} = \begin{pmatrix} u_1 + v_1 \\ u_2 + v_2 \end{pmatrix}$.

**What about scalar multiplication?**

> Multiply each component by the scalar. If $c$ is a scalar, $c \vec{v} = \begin{pmatrix} c v_1 \\ c v_2 \end{pmatrix}$.

**Example: $\vec{u} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$, $\vec{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$, and $c = 2$**.

> $\vec{u} + \vec{v} = \begin{pmatrix} 1 + 3 \\ 2 + 4 \end{pmatrix} = \begin{pmatrix} 4 \\ 6 \end{pmatrix}$.
   $c \vec{v} = 2 \begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} 6 \\ 8 \end{pmatrix}$.

Excellent!

## Chapter 3: Dot Product and Cross Product

**What is the dot product?**

> A scalar representing the product of two vectors' magnitudes and the cosine of the angle between them.

**Formula?**

> $\vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n$.

**Example: $\vec{u} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$ and $\vec{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$**.

> $\vec{u} \cdot \vec{v} = 1 \cdot 3 + 2 \cdot 4 = 3 + 8 = 11$.

**What about the cross product?**

> It’s a vector perpendicular to both $\vec{u}$ and $\vec{v}$ in 3D.

**Formula?**

> $\vec{u} \times \vec{v} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix}$.

**Example: $\vec{u} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ and $\vec{v} = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}$**.

> $\vec{u} \times \vec{v} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & 3 \\ 4 & 5 & 6 \end{vmatrix} = \hat{i}(2 \cdot 6 - 3 \cdot 5) - \hat{j}(1 \cdot 6 - 3 \cdot 4) + \hat{k}(1 \cdot 5 - 2 \cdot 4) = \begin{pmatrix} -3 \\ 6 \\ -3 \end{pmatrix}$.

Well done!

## Chapter 4: Matrices and Matrix Operations

**What is a matrix?**

> A rectangular array of numbers arranged in rows and columns.

**How do we write it?**

> $\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$.

**What is matrix addition?**

> Add corresponding elements. $\mathbf{A} + \mathbf{B} = \begin{pmatrix} a_{ij} + b_{ij} \end{pmatrix}$.

**Scalar multiplication?**

> Multiply each element by the scalar. $c \mathbf{A} = \begin{pmatrix} c a_{ij} \end{pmatrix}$.

**What is matrix multiplication?**

> The dot product of rows of the first matrix with columns of the second.

**Example: $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and $\mathbf{B} = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$**.

> $\mathbf{A} \mathbf{B} = \begin{pmatrix} 1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\ 3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$.

Excellent!

## Chapter 5: Determinants and Inverses

**What is a determinant?**

> A scalar value that can be computed from the elements of a square matrix.

**How do we find it for a 2x2 matrix?**

> For $\mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $\det(\mathbf{A}) = ad - bc$.

**Example: $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$**.

> $\det(\mathbf{A}) = 1 \cdot 4 - 2 \cdot 3 = 4 - 6 = -2$.

**What is an inverse matrix?**

> A matrix $\mathbf{A}^{-1}$ such that $\mathbf{A} \mathbf{A}^{-1} = \mathbf{I}$, where $\mathbf{I}$ is the identity matrix.

**How do we find it for a 2x2 matrix?**

> $\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$.

**Example: $\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$**.

> $\mathbf{A}^{-1} = \frac{1}{-2} \begin{pmatrix} 4 & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{pmatrix}$.

Perfect!

## Chapter 6: Vector Spaces

**What is a vector space?**

> A set of vectors with two operations: vector addition and scalar multiplication, satisfying certain axioms.

**What are those axioms?**

> Closure, associativity, commutativity, identity, inverses, distributivity, and compatibility of scalar multiplication.

**Give an example of a vector space.**

> $\mathbb{R}^2$ with standard addition and scalar multiplication.

**What is a subspace?**

> A subset of a vector space that is also a vector space under the same operations.

**Example?**

> The set of all vectors on a line through the origin in $\mathbb{R}^2$.

Excellent!

## Chapter 7: Eigenvalues and Eigenvectors

**What is an eigenvalue?**

> A scalar $\lambda$ such that for a square matrix $\mathbf{A}$ and a non-zero vector $\vec{v}$, $\mathbf{A} \vec{v} = \lambda \vec{v}$.

**What is an eigen

vector?**

> The vector $\vec{v}$ in the equation $\mathbf{A} \vec{v} = \lambda \vec{v}$.

**How do we find eigenvalues?**

> Solve $\det(\mathbf{A} - \lambda \mathbf{I}) = 0$.

**Example: $\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$**.

> $\det(\mathbf{A} - \lambda \mathbf{I}) = \begin{vmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{vmatrix} = (2 - \lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0$.

**Solve for $\lambda$.**

> $\lambda = 1, 3$.

**Find the eigenvectors.**

> For $\lambda = 1$: $\mathbf{A} - \mathbf{I} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, solution $\vec{v} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.
   For $\lambda = 3$: $\mathbf{A} - 3\mathbf{I} = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}$, solution $\vec{v} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

Well done!

## Chapter 8: Linear Transformations

**What is a linear transformation?**

> A mapping $T: \mathbb{R}^n \to \mathbb{R}^m$ that preserves vector addition and scalar multiplication.

**Example?**

> $T(\vec{x}) = \mathbf{A} \vec{x}$, where $\mathbf{A}$ is a matrix.

**What properties do linear transformations have?**

> Linearity: $T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v})$ and $T(c \vec{u}) = c T(\vec{u})$.

**Find the matrix of the linear transformation $T$ given by $T(x, y) = (x + y, x - y)$.**

> $\mathbf{A} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.

**Apply $T$ to $\vec{v} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$.**

> $T(\vec{v}) = \mathbf{A} \vec{v} = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 5 \\ -1 \end{pmatrix}$.

Perfect!

## Chapter 9: Inner Product Spaces

**What is an inner product space?**

> A vector space with an additional structure called an inner product.

**What is an inner product?**

> A generalization of the dot product, denoted $\langle \vec{u}, \vec{v} \rangle$.

**Properties?**

> Linearity, symmetry, and positive-definiteness.

**Example in $\mathbb{R}^n$?**

> $\langle \vec{u}, \vec{v} \rangle = u_1 v_1 + u_2 v_2 + \cdots + u_n v_n$.

**What is orthogonality?**

> Two vectors $\vec{u}$ and $\vec{v}$ are orthogonal if $\langle \vec{u}, \vec{v} \rangle = 0$.

**Example:**

> In $\mathbb{R}^2$, $\vec{u} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and $\vec{v} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ are orthogonal.

Excellent!

## Chapter 10: Diagonalization

**What is diagonalization?**

> The process of finding a diagonal matrix $\mathbf{D}$ similar to a given square matrix $\mathbf{A}$.

**Why is it useful?**

> Diagonal matrices are easier to work with, especially for computing powers and exponentials of matrices.

**How do we diagonalize a matrix?**

> Find a matrix $\mathbf{P}$ of eigenvectors such that $\mathbf{P}^{-1} \mathbf{A} \mathbf{P} = \mathbf{D}$, where $\mathbf{D}$ is diagonal.

**Example:**

> Given $\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, with eigenvalues $\lambda = 1, 3$ and corresponding eigenvectors $\vec{v}_1 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$ and $\vec{v}_2 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.

**Construct $\mathbf{P}$ and $\mathbf{D}$:**

> $\mathbf{P} = \begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$, $\mathbf{D} = \begin{pmatrix} 1 & 0 \\ 0 & 3 \end{pmatrix}$.

Perfect!

**Are you ready to explore more?**

> Absolutely!

**Happy vectoring!**

---

**End of The Little Linear Algebra**

