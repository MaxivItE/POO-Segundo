from ClaseLadrillo import Ladrillo
from ClaseMaterialRefractario import MaterialRefractario
from GestorPedidosLadrillos import PedidoLadrillos

def test(gestor_ladrillos, gestor_material_refractario):
    ladrillo1 = Ladrillo(45, 2, 500.20, 6000)
    ladrillo2 = Ladrillo(20, 4, 250.65, 5500)
    ladrillo3 = Ladrillo(15, 5, 1250.20, 10000)
    ladrillo4 = Ladrillo(18, 1, 100.65, 9800)
    material_refractario1 = MaterialRefractario("Sílice", "Sin caracteristicas", 30.20, 2000)
    material_refractario2 = MaterialRefractario("Alúmina", "Sin caracteristicas", 60.61, 900)
    material_refractario3 = MaterialRefractario("Magnesia", "Sin caracteristicas", 40.10, 1200)
    material_refractario4 = MaterialRefractario("Chamota", "Sin caracteristicas", 35.00, 1600)
    gestor_material_refractario.agregarMaterialRefractario(material_refractario1)
    gestor_material_refractario.agregarMaterialRefractario(material_refractario2)
    gestor_material_refractario.agregarMaterialRefractario(material_refractario3)
    gestor_material_refractario.agregarMaterialRefractario(material_refractario4)
    pedido_ladrillos1 = PedidoLadrillos(ladrillo1, material_refractario3)
    pedido_ladrillos2 = PedidoLadrillos(ladrillo2, material_refractario1)
    pedido_ladrillos3 = PedidoLadrillos(ladrillo3)
    pedido_ladrillos4 = PedidoLadrillos(ladrillo4)
    gestor_ladrillos.agregarPedido(pedido_ladrillos1)
    gestor_ladrillos.agregarPedido(pedido_ladrillos2)
    gestor_ladrillos.agregarPedido(pedido_ladrillos3)
    gestor_ladrillos.agregarPedido(pedido_ladrillos4)