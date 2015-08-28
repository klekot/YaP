namespace SEOShow
{
    partial class Form1
    {
        /// <summary>
        /// Требуется переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Обязательный метод для поддержки конструктора - не изменяйте
        /// содержимое данного метода при помощи редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.rtbYandex = new System.Windows.Forms.RichTextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.rtbGoogle = new System.Windows.Forms.RichTextBox();
            this.tbZapros = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.tbSite = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.button2 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(123, 296);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 1;
            this.button1.Text = "Париснг";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label1.Location = new System.Drawing.Point(49, 65);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(61, 17);
            this.label1.TabIndex = 4;
            this.label1.Text = "Yandex";
            // 
            // rtbYandex
            // 
            this.rtbYandex.Location = new System.Drawing.Point(12, 85);
            this.rtbYandex.Name = "rtbYandex";
            this.rtbYandex.Size = new System.Drawing.Size(138, 193);
            this.rtbYandex.TabIndex = 3;
            this.rtbYandex.Text = "";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.label2.Location = new System.Drawing.Point(208, 65);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(60, 17);
            this.label2.TabIndex = 6;
            this.label2.Text = "Google";
            // 
            // rtbGoogle
            // 
            this.rtbGoogle.Location = new System.Drawing.Point(171, 85);
            this.rtbGoogle.Name = "rtbGoogle";
            this.rtbGoogle.Size = new System.Drawing.Size(138, 193);
            this.rtbGoogle.TabIndex = 5;
            this.rtbGoogle.Text = "";
            // 
            // tbZapros
            // 
            this.tbZapros.Location = new System.Drawing.Point(12, 31);
            this.tbZapros.Name = "tbZapros";
            this.tbZapros.Size = new System.Drawing.Size(138, 20);
            this.tbZapros.TabIndex = 7;
            this.tbZapros.Text = "парсер на c#";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 15);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(44, 13);
            this.label3.TabIndex = 8;
            this.label3.Text = "Запрос";
            // 
            // tbSite
            // 
            this.tbSite.Location = new System.Drawing.Point(171, 31);
            this.tbSite.Name = "tbSite";
            this.tbSite.Size = new System.Drawing.Size(138, 20);
            this.tbSite.TabIndex = 9;
            this.tbSite.Text = "http://jobtools.ru";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(168, 15);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(81, 13);
            this.label4.TabIndex = 10;
            this.label4.Text = "Искомый сайт";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(234, 296);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 11;
            this.button2.Text = "button2";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(338, 340);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.tbSite);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.tbZapros);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.rtbGoogle);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.rtbYandex);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Парсер";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.RichTextBox rtbYandex;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.RichTextBox rtbGoogle;
        private System.Windows.Forms.TextBox tbZapros;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox tbSite;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button button2;
    }
}

