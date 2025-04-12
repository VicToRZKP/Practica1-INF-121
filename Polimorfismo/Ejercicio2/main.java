package eje3;

public class main {
	
	public static void main(String[] args) {
		Cocinero a = new Cocinero();
		a.mostrar();
		a.sueldoTotal();
		a.mostrar(1200);

		Mesero b = new Mesero("Pedro", 1000, 10, 50, 200);
		b.mostrar();
		b.sueldoTotal();
		b.mostrar(1200);

		Mesero c = new Mesero();
		c.mostrar();
		c.sueldoTotal();
		c.mostrar(1200);

		Administrativo d = new Administrativo("Jose", 1000, "Gerente");
		d.mostrar();
		d.sueldoTotal();
		d.mostrar(1200);

		Administrativo e = new Administrativo();
		e.mostrar();
		e.sueldoTotal();
		e.mostrar(1500);

	}
}
