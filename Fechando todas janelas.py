import pygetwindow as gw

# Obtém todas as janelas abertas
windows = gw.getAllWindows()

# Fecha todas as janelas visíveis
for window in windows:
    if window.visible:
        window.close()
print(f"Janela '{window.title}' fechada.")
