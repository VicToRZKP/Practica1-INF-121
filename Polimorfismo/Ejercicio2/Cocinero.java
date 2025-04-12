package eje3;

public class Cocinero {
	 private String nombre;
	 private int sueldoMes , hrsExtra;
	 private float sueldoHora;
	
	public Cocinero() {
		nombre="juan";
		sueldoMes= 1200;
		hrsExtra=10;
		sueldoHora =15;
	}
	public Cocinero(String n,int sm,int he,float sh) {
		nombre=n;
		sueldoMes=sm;
		hrsExtra=he;
		sueldoHora=sh;
	}
	public double sueldoTotal() {
		double st=sueldoMes+(sueldoHora*hrsExtra);
		return st;
	}
	public void mostrar() {
		System.out.println("--------cosinero-------");
		System.out.println("nombre:"+nombre);
		System.out.println("sueldo mes:"+sueldoMes);
		System.out.println("hrs extra: "+hrsExtra);
		System.out.println("sueldo hora:"+sueldoHora);
		System.out.println("sueldo total: "+sueldoTotal());
	}
	public void mostrar(float x) {
		if (sueldoMes==x) {
			System.out.println("--------el cocinero con sueldo igual a x es:-------");
			System.out.println("nombre:"+nombre);
			System.out.println("sueldo mes:"+sueldoMes);
			System.out.println("hrs extra: "+hrsExtra);
			System.out.println("sueldo hora:"+sueldoHora);
			System.out.println("sueldo total: "+sueldoTotal());
		}
		else {
			System.out.println("no se encontro ningun cosinero que gane igual a "+x);
		}
	}
}
