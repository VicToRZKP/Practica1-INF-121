package ejercicio1;
public class main1 {

	public static void main(String[] args) {
		Persona a=new Persona ("juan","el alto",12);
		a.saludo();
		System.out.println(a.mayordeEdad());
		Persona b=new Persona ("melany","beni",75);
		b.saludo();
		System.out.println(b.mayordeEdad());
		Persona c=new Persona ("pepe","santa cruz",52);
		c.saludo();
		System.out.println(c.mayordeEdad());
	}
}
