# Instrucciones para Integrar el Mapa de Elementor

Para integrar la sección de ubicación (mapa) de `https://mercacol.com.co/elementor-993/` directamente dentro de `riviera.html` en lugar de abrirla en una nueva pestaña, puedes utilizar un `iframe`.

A continuación, te mostramos cómo hacerlo:

### 1. Código HTML

Puedes reemplazar la sección actual de ubicación o agregar una nueva sección con el siguiente código:

```html
<section id="ubicacion-elementor" class="py-20 bg-gray-50 relative">
    <div class="container mx-auto px-6">
        <div class="text-center mb-10" data-aos="fade-up">
            <h2 class="text-3xl md:text-4xl font-serif font-bold text-brand-blue mb-2">
                Nuestra <span class="text-brand-gold">Ubicación</span>
            </h2>
            <p class="text-gray-600">Explora el entorno de Riviera del Occidente.</p>
        </div>

        <!-- Contenedor del Iframe -->
        <div class="w-full h-[600px] rounded-2xl overflow-hidden shadow-2xl border-4 border-white" data-aos="zoom-in">
            <iframe
                src="https://mercacol.com.co/elementor-993/"
                width="100%"
                height="100%"
                style="border:0;"
                allowfullscreen=""
                loading="lazy"
                title="Mapa de Ubicación Riviera del Occidente">
            </iframe>
        </div>
    </div>
</section>
```

### 2. Consideraciones Importantes

*   **Responsividad:** El contenedor del iframe está configurado con `w-full` (ancho completo) y una altura fija de `h-[600px]`. Puedes ajustar esta altura según sea necesario para dispositivos móviles (por ejemplo, `h-[400px] md:h-[600px]`).
*   **Velocidad de Carga:** Cargar una página completa de WordPress dentro de un iframe puede afectar ligeramente el tiempo de carga inicial de tu página `riviera.html`. El atributo `loading="lazy"` ayuda a mitigar esto cargando el iframe solo cuando el usuario se acerca a la sección.
*   **Estilos del Sitio Externo:** Ten en cuenta que el diseño dentro del iframe (fuentes, colores, márgenes) dependerá totalmente de la página `https://mercacol.com.co/elementor-993/` y no heredará los estilos de `riviera.html`.
*   **Permisos (X-Frame-Options):** Actualmente, el sitio `mercacol.com.co` permite ser embebido. Si en el futuro el administrador del sitio cambia la configuración de seguridad (`X-Frame-Options` o `Content-Security-Policy`), el iframe podría dejar de funcionar.

### 3. Alternativa Nativa (Recomendada)

Si deseas un mayor control sobre el diseño y la velocidad, te recomendamos recrear la sección utilizando los componentes nativos de `riviera.html` (Tailwind CSS + Google Maps Embed API), como ya se encuentra implementado parcialmente en la sección `#ubicacion` actual. Esto garantiza una experiencia de usuario más fluida y coherente visualmente.
