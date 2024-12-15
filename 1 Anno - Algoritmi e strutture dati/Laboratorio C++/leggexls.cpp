#include <iostream>
#include <libxlsx/xlsx.h>

int main() {
    xlsx_workbook* wb = xlsx_open("AppelliEsame.xlsx");
    if (wb) {
        xlsx_worksheet* sheet = xlsx_workbook_worksheet(wb, 0); // Primo foglio
        // Leggi i dati dal foglio
        for (int row = 0; row < xlsx_worksheet_rows(sheet); row++) {
            for (int col = 0; col < xlsx_worksheet_cols(sheet); col++) {
                const char* value = xlsx_cell_value(sheet, row, col);
                std::cout << value << " ";
            }
            std::cout << std::endl;
        }
        xlsx_close(wb);
    } else {
        std::cerr << "Errore nell'apertura del file" << std::endl;
    }
    return 0;
}