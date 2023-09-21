Public Class clsproject
    Public Function hitungdimensi(param1 As String, param2 As String) As Double

        If Not IsNumeric(param1) Or Not IsNumeric(param2) Then
            MsgBox("Data Parameter Salah!")
            Return 0
            Exit Function
        End If

        Dim hasil As Double = param1 * param2
        Return hasil
        hitungdimensi = hasil

    End Function

End Class
