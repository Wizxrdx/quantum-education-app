import flet as ft
import qiskit.qasm2
import qiskit_aer


class QuantumEducationApp:
    def __init__(self, page: ft.Page):
        self.__page = page

        self.__title = "Quantum Education App"
        self.__input = ft.TextField(
            label="Code Editor",
            value="",
            multiline=True,
            border_radius=ft.border_radius.all(5),
            focused_border_color=ft.colors.BLUE,
            focused_border_width=2,
        )
        self.__simulate_button = ft.FilledButton(text="Simulate", on_click=self.simulate)
        self.__output = ft.TextField(
            read_only=True,
            label="Output Here",
            value="",
            multiline=True,
            height=200,
            border_radius=ft.border_radius.all(5),
            focused_border_color=ft.colors.BLUE,
            focused_border_width=2,
        )

        self.__page.add(
            ft.Column(
                [
                    self.__input,
                    self.__simulate_button,
                    self.__output
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

        self.__page.controls.append(self.__output)

    def simulate(self, e):
        '''
        OPENQASM 2.0;
        include "qelib1.inc";
        qreg q[2];
        creg c[2];

        h q[0];
        cx q[0], q[1];

        measure q -> c;
        '''
        program = self.__input.value
        circuit = qiskit.qasm2.loads(program)
        # output = circuit.draw('latex')

        job = qiskit_aer.QasmSimulator().run(circuit, shots=100)
        result = job.result()
        output = result.get_counts()
        print(result.get_counts())

        self.__output.value = str(output)
        self.__page.update()
