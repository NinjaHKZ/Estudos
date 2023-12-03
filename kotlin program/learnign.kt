// coding: utf-8

class SimpleAssistante(username: String? = null, age: String? = null){
    var name: String
    var dailyProduction: String
    var userName: String
    var userAge: String
    
    init {
        name = "Simple Test"
        dailyProduction = "03/12/20203"
        
        userName = username ?: "guest"
        userAge = age ?: "not defined"
        println("complete. Wellcome $userName :)")
        
    }

    fun logicalBrain(recived: String): String {
        Runtime.getRuntime().exec("explorer")
        return when {
            recived in listOf("oi", "olá", "olá tudo bem?", "iae", "iae mano") -> "Iae! Como que tu ta meu caro $userName? :)"
            recived in listOf("dados", "dados coletados", "retorne minhas informações", "retorne informações definidas") -> {
                var data = mutableListOf<String>()

                for(item in getInformationsPassed()){
                    data.add("\n\t--->${item.key} = ${item.value}")
                }
                "\nclaro, aqui está: ${data.joinToString()}"
            }
            else -> "ainda não fui treinado para isso :("
        }
        
    }

    fun getInformationsPassed(): Map<String, String> { 
        return mapOf("name" to name, "dailyProduction" to dailyProduction, "userName" to userName, "userAge" to userAge)
    }
}




fun main(){
    println("\n\nAssistent is Starting, Please wait...")
    var recive = "dados"
    println(SimpleAssistante().logicalBrain(recived=recive))
}
