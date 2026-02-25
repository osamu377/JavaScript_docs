Attribute VB_Name = "Module2"
Sub Macro2()
Attribute Macro2.VB_ProcData.VB_Invoke_Func = " \n14"
'
' Macro2 Macro
'

'
    With Selection.Font
        .Color = -16776961
        .TintAndShade = 0
    End With
End Sub

Sub Macro3()
Attribute Macro3.VB_ProcData.VB_Invoke_Func = " \n14"
'
' Macro3 Macro
'

'
    Range("B1").Font.Color = -16776961
    
End Sub
Sub Macro4()
Attribute Macro4.VB_ProcData.VB_Invoke_Func = " \n14"
'
' Macro4 Macro
'

'
    With Selection.Interior
        .Pattern = xlSolid
        .PatternColorIndex = xlAutomatic
        .Color = 65535
        .TintAndShade = 0
        .PatternTintAndShade = 0
    End With
    Range("B2").Select
    With Selection.Font
        .Color = -16711681
        .TintAndShade = 0
    End With
    With Selection.Font
        .Color = -4165632
        .TintAndShade = 0
    End With
    Range("D3").Select
End Sub
