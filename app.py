import flet as ft

def main(page: ft.Page):
    page.title = "CV - Bryann Gutierrez Salcedo"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0E1117"  # Fondo oscuro profundo moderno
    page.padding = 30
    page.window_width = 1150
    page.window_height = 850
    page.window_resizable = True

    # --- ESTILOS COMPARTIDOS ---
    COLOR_PRIMARIO = "#00D2FF"  # Cyan eléctrico
    COLOR_ACCENTO = "#0072FF"   # Azul moderno
    COLOR_BG_CARD = "#161B22"   # Gris oscuro para tarjetas
    
    BORDE_ESTABLE = ft.Border(
        top=ft.BorderSide(1, ft.Colors.GREY_800),
        bottom=ft.BorderSide(1, ft.Colors.GREY_800),
        left=ft.BorderSide(1, ft.Colors.GREY_800),
        right=ft.BorderSide(1, ft.Colors.GREY_800)
    )
    
    content_area = ft.Container(expand=True, animate_opacity=300)

    # --- PESTAÑA: PERFIL ---
    def show_perfil(e=None):
        content_area.content = ft.Column([
            ft.Text("Perfil Profesional", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Text(
                "Ingeniero Electrónico egresado de la Universidad Pedagógica y Tecnológica de Colombia, con sólida "
                "trayectoria en el diseño, desarrollo e integración de sistemas de software full-stack y soluciones de hardware/firmware "
                "para IoT y control industrial. Investigador coautor en tecnologías de redes de sensores inalámbricas con publicación "
                "internacional indexada (IEEE). Perfil integral con experiencia en gestión de proyectos de infraestructura tecnológica, "
                "sistemas de seguridad electrónica, redes TCP/IP y soluciones de energía solar fotovoltaica.",
                size=15, color=ft.Colors.GREY_400
            ),
            ft.Divider(color=ft.Colors.GREY_800, height=25),
            ft.Text("Educación Académica", size=20, weight=ft.FontWeight.BOLD),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.SCHOOL, color=COLOR_PRIMARIO, size=28),
                title=ft.Text("Ingeniería Electrónica", weight=ft.FontWeight.BOLD),
                subtitle=ft.Text("Universidad Pedagógica y Tecnológica de Colombia (UPTC) • Graduado: Diciembre 2022\n"
                                 "Énfasis en gestión de proyectos, energías renovables y desarrollo de software/hardware. "
                                 "Monografía calificada como 'Satisfactorio' (Acta No. SOG 245)."),
            ),
            ft.Divider(color=ft.Colors.GREY_800, height=25),
            ft.Text("Publicaciones Científicas", size=20, weight=ft.FontWeight.BOLD),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.MENU_BOOK, color=COLOR_ACCENTO, size=28),
                title=ft.Text("IEEE Research Contribution - Investigador Autor", weight=ft.FontWeight.BOLD),
                subtitle=ft.Text("Artículo: 'Wearable Prototype for the Measurement of Explosive Gases in Mining'\n"
                                 "Conferencia: 2nd International Conference on Machine Learning and Applied Network Technologies\n"
                                 "Avalado por: IEEE El Salvador Section | Diciembre 2021"),
            )
        ], scroll=ft.ScrollMode.AUTO, spacing=15)
        page.update()

    # --- PESTAÑA: EXPERIENCIA ---
    def show_experiencia(e=None):
        content_area.content = ft.Column([
            ft.Text("Trayectoria Profesional", size=26, weight=ft.FontWeight.BOLD),
            
            # P&M S.A.S
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Ingeniero de Proyectos y Desarrollo (Software / Infraestructura)", size=16, weight=ft.FontWeight.BOLD),
                        ft.Container(ft.Text("Mar 2024 - Nov 2024", color=ft.Colors.BLACK, size=11, weight=ft.FontWeight.BOLD), 
                                     bgcolor=COLOR_PRIMARIO, padding=5, border_radius=5)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Text("Procesos de Ingeniería P&M S.A.S", color=COLOR_PRIMARIO, size=14, weight=ft.FontWeight.W_500),
                    ft.Text("• Desarrollo Full-Stack: Creación y administración de bases de datos relacionales en MySQL y desarrollo de interfaces front-end y back-end para adquisición de datos y acceso remoto.\n"
                            "• Automatización & Control: Programación de sistemas embebidos utilizando microcontroladores, FPGA y PLCs para la instrumentación de sensores y actuadores en sistemas de riego automatizados.\n"
                            "• Seguridad Electrónica & Energía Solar: Diseño e implementación de sistemas solares fotovoltaicos autónomos para redes críticas de CCTV, alarmas y controles de acceso biométricos.\n"
                            "• Obras Civiles: Revisión, diseño y ajuste de planos eléctricos, cableado de redes y supervisión técnica en viviendas y oficinas.", 
                            color=ft.Colors.GREY_400, size=13)
                ]),
                bgcolor=COLOR_BG_CARD, padding=20, border_radius=15, border=BORDE_ESTABLE
            ),
            
            # UPTC Práctica
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Ingeniero de Investigación y Desarrollo (Práctica Laboral)", size=16, weight=ft.FontWeight.BOLD),
                        ft.Container(ft.Text("Ago 2021 - Ago 2022", color=ft.Colors.WHITE, size=11, weight=ft.FontWeight.BOLD), 
                                     bgcolor=COLOR_ACCENTO, padding=5, border_radius=5)
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Text("Universidad Pedagógica y Tecnológica de Colombia", color=COLOR_ACCENTO, size=14, weight=ft.FontWeight.W_500),
                    ft.Text("• Prototipado IoT Avanzado: Diseño e integración de una red de sensores para medición de gases explosivos en minería subterránea mediante tecnología inalámbrica LoRa (SX1278).\n"
                            "• Diseño de Hardware (PCB): Creación de diagramas esquemáticos y ruteo de circuitos impresos multinivel utilizando Proteus y KiCad (gestión de carga y baterías).\n"
                            "• Desarrollo de Firmware: Programación en lenguaje C bajo entornos MPLAB IDE para la optimización de lectura de variables y potencia de transmisión de red.\n"
                            "• Software & Modelos de Datos: Interfaz de usuario en Python (Tkinter) para comunicación serial y uso de Pandas/NumPy para el desarrollo de modelos predictivos de concentraciones de gas.", 
                            color=ft.Colors.GREY_400, size=13)
                ]),
                bgcolor=COLOR_BG_CARD, padding=20, border_radius=15, border=BORDE_ESTABLE
            )
        ], spacing=20, scroll=ft.ScrollMode.AUTO)
        page.update()

    # --- PESTAÑA: HABILIDADES ---
    def show_habilidades(e=None):
        def skill_bar(name, level):
            return ft.Container(
                content=ft.Column([
                    ft.Row([ft.Text(name, weight=ft.FontWeight.BOLD, size=13), ft.Text(f"{int(level*100)}%")], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.ProgressBar(value=level, color=COLOR_PRIMARIO, bgcolor=ft.Colors.GREY_800, height=6)
                ]),
                col={"sm": 6}
            )

        content_area.content = ft.Column([
            ft.Text("Habilidades Tecnológicas", size=26, weight=ft.FontWeight.BOLD),
            ft.Text("Software & Data", size=16, color=COLOR_PRIMARIO, weight=ft.FontWeight.W_600),
            ft.ResponsiveRow([
                skill_bar("Python (Tkinter / Pandas / NumPy)", 0.90),
                skill_bar("Arquitectura Full-Stack & SQL (MySQL)", 0.85),
                skill_bar("Git / GitHub & Servidores Remotos", 0.85),
            ], run_spacing=15),
            
            ft.Divider(color=ft.Colors.GREY_800, height=30),
            ft.Text("Hardware & Firmware", size=16, color=COLOR_PRIMARIO, weight=ft.FontWeight.W_600),
            ft.ResponsiveRow([
                skill_bar("Lenguaje C / MPLAB IDE / Microcontroladores", 0.92),
                skill_bar("Diseño PCB (KiCad / Proteus)", 0.90),
                skill_bar("Módulos de RF / LoRa (SX1278) / FPGAs / PLCs", 0.80),
            ], run_spacing=15),
            
            ft.Divider(color=ft.Colors.GREY_800, height=30),
            ft.Text("Infraestructura & Automatización", size=16, color=COLOR_PRIMARIO, weight=ft.FontWeight.W_600),
            ft.Row([
                ft.Chip(label=ft.Text("Redes TCP/IP")),
                ft.Chip(label=ft.Text("CCTV & Seguridad Electrónica")),
                ft.Chip(label=ft.Text("Acceso Biométrico")),
                ft.Chip(label=ft.Text("Energía Solar Fotovoltaica")),
                ft.Chip(label=ft.Text("Planos Eléctricos (RETIE)")),
                ft.Chip(label=ft.Text("Instrumentación Agrícola")),
            ], wrap=True)
        ], spacing=15, scroll=ft.ScrollMode.AUTO)
        page.update()

    # --- PANEL LATERAL IZQUIERDO (INFORMACIÓN FIJA) ---
    sidebar = ft.Container(
        content=ft.Column([
            # Imagen de perfil con recorte circular y ajuste seguro de "cover" mediante cadena de texto
            ft.Container(
                content=ft.Image(
                    src="bryann_perfil.png",
                    fit="cover",  # <--- CORREGIDO: Uso de string nativo compatible
                    border_radius=45
                ),
                alignment=ft.Alignment(0, 0),
                width=90, height=90,
                shape=ft.BoxShape.CIRCLE,
                padding=3,
                gradient=ft.LinearGradient([COLOR_PRIMARIO, COLOR_ACCENTO])
            ),
            ft.Text("Bryann Gutierrez S.", size=20, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Text("Ingeniero Electrónico", size=13, color=COLOR_PRIMARIO, weight=ft.FontWeight.W_600),
            ft.Text("Matrícula: CN206-167287 (Vigente)", size=11, color=ft.Colors.GREY_400),
            
            ft.Divider(color=ft.Colors.GREY_800, height=20),
            
            # Datos de contacto[cite: 1]
            ft.Row([ft.Icon(ft.Icons.PHONE, color=ft.Colors.GREY_500, size=16), ft.Text("+57 310 2159370", size=12)]),
            ft.Row([ft.Icon(ft.Icons.EMAIL, color=ft.Colors.GREY_500, size=16), ft.Text("brags@outlook.es", size=12)]),
            ft.Row([ft.Icon(ft.Icons.LOCATION_ON, color=ft.Colors.GREY_500, size=16), ft.Text("Tunja, Boyacá, Col", size=12)]),
            ft.Row([ft.Icon(ft.Icons.LANGUAGE, color=ft.Colors.GREY_500, size=16), ft.Text("bryannquti.github.io/...", size=12)]),
            
            ft.Divider(color=ft.Colors.GREY_800, height=20),
            
            # Menú
            ft.TextButton("PERFIL", icon=ft.Icons.PERSON, on_click=show_perfil, style=ft.ButtonStyle(color=ft.Colors.WHITE)),
            ft.TextButton("EXPERIENCIA", icon=ft.Icons.WORK, on_click=show_experiencia, style=ft.ButtonStyle(color=ft.Colors.WHITE)),
            ft.TextButton("TECNOLOGÍAS", icon=ft.Icons.CODE, on_click=show_habilidades, style=ft.ButtonStyle(color=ft.Colors.WHITE)),
            
            ft.Divider(color=ft.Colors.GREY_800, height=20),
            # Badge de Situación Legal / Militar[cite: 1]
            ft.Container(
                content=ft.Column([
                    ft.Text("Legal & Ley", size=11, weight=ft.FontWeight.BOLD, color=COLOR_PRIMARIO),
                    ft.Text("Reservista de 1ra Clase\nConducta: Excelente", size=10, color=ft.Colors.GREY_400)
                ], spacing=2),
                padding=8, bgcolor="#1A2333", border_radius=8
            )
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        width=260,
        bgcolor=COLOR_BG_CARD,
        padding=20,
        border_radius=20,
        border=BORDE_ESTABLE
    )

    # --- LAYOUT PRINCIPAL ---
    layout = ft.Row(
        [
            sidebar,
            ft.VerticalDivider(width=5, color=ft.Colors.TRANSPARENT),
            ft.Container(
                content=content_area,
                expand=True,
                bgcolor=COLOR_BG_CARD,
                padding=25,
                border_radius=20,
                border=BORDE_ESTABLE
            )
        ],
        expand=True
    )

    page.add(layout)
    show_perfil()

ft.app(target=main)