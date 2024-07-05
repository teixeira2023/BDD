import pytest

# Função simulada para alternar o estado da luz da cabine
def toggle_cabin_light(initial_state, power_mode, range_selection, toggle_button):
    if range_selection == 'Park' and power_mode > 10 and toggle_button == 'press':
        return 'on' if initial_state == 'off' else 'off'
    return initial_state

@pytest.mark.parametrize("initial_state, final_state", [
    ("off", "on"),
    ("on", "off"),
])
def test_turn_on_cabin_light(initial_state, final_state):
    power_mode = 20  # Exemplo de valor válido para o modo de potência
    range_selection = 'Park'
    toggle_button = 'press'
    
    result = toggle_cabin_light(initial_state, power_mode, range_selection, toggle_button)
    
    assert result == final_state, f"Erro: Esperado {final_state}, mas obtido {result}"
