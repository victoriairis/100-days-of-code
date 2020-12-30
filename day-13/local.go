package local

import "fmt"

func local(nome, cidade string) (regiao, estado string){
	switch cidade {
	case "Mossoró","Natal":
		estado = "RN"

	case "Aracaju":
		estado = "SE"

	default: 
		estado = "DESCONHECIDO"
	}
	return
}

func main(){
	regiao, estado := local("iris", "Mossoró")
	fmt.Printf("%s mora em %s", regiao, estado)
}