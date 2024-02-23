fun main(){
        // --open-formatter-skip-next-line
        println( "Testcase number 6" )

        // Format blocks without {} and also linear
        for(i in 1..5)
        for (j in 1..5)
        for    (k in 1..5)
        println("$i $j $k")

        // REASON: if we have multiple `for` with space
        for  (k in 1..5)
        println("$k")

        for(k in 1..5)println("$k")

        // REASON: if we have multiple `while` with space
        var x=4
        while    (x-->0)
        println(x)

        // REASON: if we have multiple `while` inside each other
        var  y  =  6
        var  t  =  3
        while(y-->0)while(t-->0)println(y)
}