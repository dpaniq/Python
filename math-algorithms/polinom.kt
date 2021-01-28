fun main () {
    val (N, K, X) = readLine()?.split(' ')!!.map{ x -> x.toInt()}
    val coefficients: List<Int> = readLine()?.split(' ')!!.map{ x -> x.toInt()}
    var kFactorial = 1

//    val N = 4
//    val K = 1
//    val X = 1
//    val coefficients: List<Int> = listOf(3, 2, -5, 1)
//    var kFactorial = 1;

    /* 2. Находим производную */


    /* 1. Находим полнином(-ы) */
    val polynomialList: MutableList<List<Int>> = mutableListOf(coefficients);
    println(polynomialList)
    for (k in 0..K) // Количество требуемых полиномов
    {
        /* Временный полином */
        val temporaryPolynomial: MutableList<Int> = mutableListOf(polynomialList[k][0])
        println("COUNT: " + polynomialList[k].count())
        for(coef in 0 until polynomialList[k].count() - 1) // Коэффициенты
        {
            val interim = (temporaryPolynomial[coef] * X) + polynomialList[k][coef + 1]
            println("$interim, $coef")
            temporaryPolynomial.add(interim)
        }
        println("Polynomial: $temporaryPolynomial")
        polynomialList.add(temporaryPolynomial)

        /* 3. Находим k! Пока цикл двигается и к != 0 */
        if (k > 0) {
            kFactorial *= k
        }
    }

    /* 4. Ответ */
    print(":kF: $kFactorial : Answer is " + (kFactorial * polynomialList.last().last()))

}
