import flet as ft

def main(page: ft.Page):
    page.title = "Mi Currículum Innovador"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0E1117"  # Fondo oscuro profundo moderno
    page.padding = 30
    page.window_width = 1100
    page.window_height = 800
    page.window_resizable = True

    # --- ESTILOS COMPARTIDOS ---
    COLOR_PRIMARIO = "#00D2FF"  # Cyan eléctrico
    COLOR_ACCENTO = "#0072FF"   # Azul moderno
    COLOR_BG_CARD = "#161B22"   # Gris oscuro para tarjetas
    
    # Borde seguro y compatible para todas las versiones de Flet
    BORDE_ESTABLE = ft.Border(
        top=ft.BorderSide(1, ft.Colors.GREY_800),
        bottom=ft.BorderSide(1, ft.Colors.GREY_800),
        left=ft.BorderSide(1, ft.Colors.GREY_800),
        right=ft.BorderSide(1, ft.Colors.GREY_800)
    )
    
    # --- CONTROLADOR DE CONTENIDO DINÁMICO ---
    content_area = ft.Container(expand=True, animate_opacity=300)

    # --- VISTAS DE LAS PESTAÑAS ---
    def show_perfil(e=None):
        content_area.content = ft.Column([
            ft.Text("Sobre Mí", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Text(
                "Desarrollador apasionado por crear soluciones tecnológicas eficientes e innovadoras. "
                "Especializado en el desarrollo de software moderno, integración de hardware/SDKs y "
                "optimización de sistemas informáticos.",
                size=16, color=ft.Colors.GREY_400
            ),
            ft.Divider(color=ft.Colors.GREY_800, height=30),
            ft.Text("Educación & Certificaciones", size=22, weight=ft.FontWeight.BOLD),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.SCHOOL, color=COLOR_PRIMARIO),
                title=ft.Text("Ingeniería de Sistemas / Ciencias de la Computación"),
                subtitle=ft.Text("Universidad Destacada • En curso / Graduado"),
            )
        ], scroll=ft.ScrollMode.AUTO)
        page.update()

    def show_experiencia(e=None):
        content_area.content = ft.Column([
            ft.Text("Trayectoria Profesional", size=28, weight=ft.FontWeight.BOLD),
            # Tarjeta de Experiencia 1
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Desarrollador Full-Stack", size=18, weight=ft.FontWeight.BOLD),
                        ft.Container(ft.Text("Actual", color=ft.Colors.BLACK, size=12, weight=ft.FontWeight.BOLD), 
                                     bgcolor=COLOR_PRIMARIO, padding=5, border_radius=5)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Text("Tech Solutions Inc. | 2025 - Presente", color=COLOR_PRIMARIO, size=14),
                    ft.Text("• Lideré el desarrollo de interfaces interactivas y arquitecturas locales de servidores.\n"
                            "• Integré con éxito sistemas biométricos y SDKs de captura de imágenes de terceros.\n"
                            "• Optimicé el rendimiento de bases de datos reduciendo tiempos de respuesta.", 
                            color=ft.Colors.GREY_400)
                ]),
                bgcolor=COLOR_BG_CARD, padding=20, border_radius=15, border=BORDE_ESTABLE
            ),
            ft.VerticalDivider(height=10),
            # Tarjeta de Experiencia 2
            ft.Container(
                content=ft.Column([
                    ft.Text("Desarrollador Junior / Freelance", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text("Proyectos Independientes | 2024 - 2025", color=COLOR_ACCENTO, size=14),
                    ft.Text("• Diseño e implementación de aplicaciones web interactivas y landing pages.\n"
                            "• Configuración de sistemas locales y automatización de tareas en Python.", 
                            color=ft.Colors.GREY_400)
                ]),
                bgcolor=COLOR_BG_CARD, padding=20, border_radius=15, border=BORDE_ESTABLE
            )
        ], spacing=20, scroll=ft.ScrollMode.AUTO)
        page.update()

    def show_habilidades(e=None):
        def skill_bar(name, level):
            return ft.Column([
                ft.Row([ft.Text(name, weight=ft.FontWeight.BOLD), ft.Text(f"{int(level*100)}%")], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.ProgressBar(value=level, color=COLOR_PRIMARIO, bgcolor=ft.Colors.GREY_800, height=8)
            ])

        content_area.content = ft.Column([
            ft.Text("Skills & Tecnologías", size=28, weight=ft.FontWeight.BOLD),
            ft.Text("Lenguajes & Frameworks", size=18, color=COLOR_PRIMARIO, weight=ft.FontWeight.W_500),
            ft.ResponsiveRow([
                ft.col({"sm": 6}, content=skill_bar("Python / Flet / FastAPI", 0.90)),
                ft.col({"sm": 6}, content=skill_bar("JavaScript / React / Node.js", 0.85)),
                ft.col({"sm": 6}, content=skill_bar("Bases de Datos (SQL/NoSQL)", 0.80)),
                ft.col({"sm": 6}, content=skill_bar("HTML5 / CSS3 / Tailwind", 0.95)),
            ], run_spacing=20),
            ft.Divider(color=ft.Colors.GREY_800, height=40),
            ft.Text("Otras Competencias", size=18, color=COLOR_PRIMARIO, weight=ft.FontWeight.W_500),
            ft.Row([
                ft.Chip(label=ft.Text("Integración de Hardware/Biometría")),
                ft.Chip(label=ft.Text("Git / GitHub")),
                ft.Chip(label=ft.Text("Arquitectura de Servidores Locales")),
                ft.Chip(label=ft.Text("Análisis de Datos")),
            ], wrap=True)
        ], spacing=15, scroll=ft.ScrollMode.AUTO)
        page.update()

    # --- PANEL LATERAL IZQUIERDO (PERFIL FIJO) ---
    sidebar = ft.Container(
        content=ft.Column([
            # Avatar centrado de forma segura mediante coordenadas exactas
            ft.Container(
                content=ft.Text("CV", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                alignment=ft.Alignment(0, 0),
                width=100, height=100,
                shape=ft.BoxShape.CIRCLE,
                gradient=ft.LinearGradient([COLOR_PRIMARIO, COLOR_ACCENTO])
            ),
            ft.Text("Tu Nombre Aquí", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Text("Full-Stack Developer", size=14, color=COLOR_PRIMARIO, weight=ft.FontWeight.W_600),
            
            ft.Divider(color=ft.Colors.GREY_800, height=30),
            
            # Datos de contacto rápidos
            ft.Row([ft.Icon(ft.Icons.EMAIL, color=ft.Colors.GREY_400, size=18), ft.Text("correo@example.com", size=13)]),
            ft.Row([ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.GREY_400, size=18), ft.Text("Tu Ciudad, País", size=13)]),
            ft.Row([ft.Icon(ft.Icons.LINK, color=ft.Colors.GREY_400, size=18), ft.Text("github.com/tu-usuario", size=13)]),
            
            ft.Divider(color=ft.Colors.GREY_800, height=30),
            
            # Botones de navegación
            ft.TextButton("SOBRE MÍ", icon=ft.Icons.PERSON, on_click=show_perfil, style=ft.ButtonStyle(color=ft.Colors.WHITE)),
            ft.TextButton("EXPERIENCIA", icon=ft.Icons.WORK, on_click=show_experiencia, style=ft.ButtonStyle(color=ft.Colors.WHITE)),
            ft.TextButton("HABILIDADES", icon=ft.Icons.CODE, on_click=show_habilidades, style=ft.ButtonStyle(color=ft.Colors.WHITE)),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        width=280,
        bgcolor=COLOR_BG_CARD,
        padding=25,
        border_radius=20,
        border=BORDE_ESTABLE
    )

    # --- DISEÑO PRINCIPAL (LAYOUT) ---
    layout = ft.Row(
        [
            sidebar,
            ft.VerticalDivider(width=10, color=ft.Colors.TRANSPARENT),
            # Contenedor derecho
            ft.Container(
                content=content_area,
                expand=True,
                bgcolor=COLOR_BG_CARD,
                padding=30,
                border_radius=20,
                border=BORDE_ESTABLE
            )
        ],
        expand=True
    )

    page.add(layout)
    
    # Cargar la primera pestaña por defecto al iniciar
    show_perfil()

ft.app(target=main)