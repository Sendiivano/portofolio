Imports png_class
Public Class Form1
    Private Sub btn_hitung_Click(sender As Object, e As EventArgs) Handles btn_hitung.Click
        Dim mclass As New png_class.clsproject

        Lpersegi.Text = mclass.hitungdimensi(pjgText.Text, lbrText.Text)




    End Sub


    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Dim mclass As New png_class.clsproject

        Llingkaran.Text = 3.14 * mclass.hitungdimensi(jaritxt.Text, jaritxt.Text)
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        Dim mclass As New png_class.clsproject
        hasil.Text = 0.5 * mclass.hitungdimensi(altxt.Text, tgtxt.Text)

    End Sub
    Private Sub hps_button(ParamArray txt() As TextBox)
        For Each tb As TextBox In txt
            tb.Text = ""
        Next
    End Sub
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        hps_button(jaritxt, Llingkaran)
    End Sub

    Private Sub hps_Click(sender As Object, e As EventArgs) Handles hps.Click

        hps_button(pjgText, lbrText, Lpersegi)
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        hps_button(altxt, tgtxt, hasil)
    End Sub
End Class
