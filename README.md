# Expense Tracker

A personal expense tracking application built with Flask that allows users to log, manage, and track their daily expenses with a beautiful notebook-style interface.

![Expense Tracker](https://img.shields.io/badge/Flask-3.1.3-green) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/expense_tracker.git
   cd expense_tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///users.db
   # For PostgreSQL production:
   # DATABASE_URL=postgresql://username:password@localhost/dbname
   ```

5. **Initialize the database**
   ```bash
   flask db upgrade
   ```

6. **Run the application**
   ```bash
   python app.py
   # or
   flask run
   ```

7. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:5000`

### Deployment

The application includes a `Procfile` for deployment on Heroku or similar platforms:

```bash
web: gunicorn app:app
```

## 📖 Project Overview

Expense Tracker is a full-stack web application that provides users with a personal expense management system. The application features user authentication, expense CRUD operations, and a beautiful notebook-themed UI that makes tracking expenses feel like writing in a personal journal.

### Key Features

- **User Authentication**: Secure registration and login system with password hashing
- **Expense Management**: Add, view, update, and delete personal expenses
- **Categorization**: Organize expenses by categories (Food, Transportation, Entertainment, Housing, Shopping, Other)
- **Total Calculation**: Automatic calculation of total expenses
- **Responsive Design**: Mobile-friendly interface that adapts to different screen sizes
- **Notebook Theme**: Unique visual design mimicking a paper notebook with ruled lines
- **Data Persistence**: SQLAlchemy ORM with support for SQLite (development) and PostgreSQL (production)

## 🎨 Styling and Design

### Visual Theme

The application features a custom **notebook theme** that creates a warm, personal journal-like experience:

- **Paper Texture Background**: Aged paper color (#f7f3e9) with subtle gradients
- **Ruled Lines**: Horizontal blue lines mimicking notebook paper
- **Red Margin Line**: Traditional notebook margin line on the left side
- **Spiral Binding**: Visual spiral binding holes along the top
- **Handwritten Fonts**: 
  - 'Caveat' for headings (playful, handwritten style)
  - 'Kalam' for body text and inputs (casual, readable handwriting)

### Color Palette

```css
--paper: #f7f3e9;           /* Main paper color */
--ink: #1c2b4a;             /* Primary text color */
--margin-line: #e05a5a;     /* Red margin line */
--rule-line: #b8cfe0;       /* Blue ruled lines */
--binding-red: #c0392b;     /* Binding color */
--green-ink: #1a6b3a;       /* Amount/money color */
--red-ink: #c0392b;         /* Error/delete color */
--blue-ink: #2c5fa8;        /* Links/primary actions */
```

### Animations

- **Page Turn**: Subtle 3D page-turn animation on load
- **Fade Up**: Elements fade in from bottom
- **Spiral Drop**: Binding holes animation
- **Hover Effects**: Buttons and links respond to hover with slight rotations

### Responsive Design

- **Desktop**: Full table layout with horizontal navigation
- **Mobile**: 
  - Hamburger menu for navigation
  - Card-style expense entries instead of table rows
  - Stacked form layouts
  - Adjusted margin line position for smaller screens

## 🏗️ System Architecture

### Architecture Pattern

The application follows a **Model-View-Controller (MVC)** pattern adapted for Flask:

- **Model**: Database models defined in `model.py`
- **View**: Jinja2 templates in `templates/` directory
- **Controller**: Route handlers in `routes.py`

### Technology Stack

- **Backend Framework**: Flask 3.1.3
- **Database ORM**: Flask-SQLAlchemy 3.1.1
- **Authentication**: Flask-Login 0.6.3
- **Form Handling**: Flask-WTF 3.1.0 with WTForms
- **Database Migrations**: Flask-Migrate 4.1.0 (Alembic)
- **Password Security**: Werkzeug security functions
- **Production Server**: Gunicorn 26.0.0
- **Environment Management**: python-dotenv 1.2.2

### Database Support

- **Development**: SQLite (default, file-based)
- **Production**: PostgreSQL (with psycopg3 driver)

## 📁 Project Structure

```
expense_tracker/
├── app.py                 # Flask application factory and configuration
├── routes.py              # All route handlers and business logic
├── model.py               # Database models (User, Expense)
├── form.py                # WTForms classes for form validation
├── wsgi.py                # WSGI entry point for production
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment configuration
├── .gitignore            # Git ignore rules
├── .env                  # Environment variables (not in git)
├── static/
│   └── css/
│       └── style.css      # Custom notebook-themed styling
├── templates/
│   ├── base.html         # Base template with common layout
│   └── auth/
│       ├── login.html    # Login page
│       └── register.html # Registration page
│   └── expenses/
│       ├── list.html     # Expense list view
│       ├── add.html      # Add expense form
│       └── update.html   # Update expense form
└── migrations/
    ├── alembic.ini       # Alembic configuration
    ├── env.py            # Migration environment
    ├── script.py.mako    # Migration template
    └── versions/
        ├── 430ce521962d_initial_migration.py
        └── 9983bde90d69_increase_password_column_length.py
```

## 🔧 Frontend Structure

### Template Hierarchy

The application uses **Jinja2 template inheritance** with a base template:

**base.html**: Provides the common layout structure
- Navigation bar with user-specific branding
- Flash message display system
- Main content area with `{% block content %}`
- CSS and meta tags

### Template Organization

Templates are organized by feature:
- `auth/` - Authentication-related pages
- `expenses/` - Expense management pages

### Form Rendering

Forms are rendered using WTForms with Jinja2:
- Automatic CSRF protection via `{{ form.hidden_tag() }}`
- Conditional error styling with form validation
- Custom styling classes for notebook theme integration

### JavaScript Integration

Minimal JavaScript used for:
- Mobile navigation toggle
- Delete confirmation dialogs
- Dynamic form interactions

## 🔌 Backend Structure

### Application Configuration (app.py)

The Flask application is configured with:
- **Secret Key**: For session security (from environment variable)
- **Database URI**: Supports both SQLite and PostgreSQL
- **Login Manager**: Configured for user authentication
- **Migration Support**: Flask-Migrate for database versioning

### Route Handlers (routes.py)

All application routes are defined in `routes.py`:

#### Authentication Routes
- `GET/POST /register` - User registration with validation
- `GET/POST /login` - User login with "Remember Me" option
- `GET /logout` - User logout and session cleanup

#### Expense Routes
- `GET /expenses` - List all user expenses with total calculation
- `GET/POST /expense/add` - Add new expense form
- `GET/POST /expense/update/<id>` - Update existing expense
- `POST /expense/delete/<id>` - Delete expense (POST only for security)

#### Utility Routes
- `GET /` - Homepage that redirects based on authentication status

### Route Protection

- **@login_required**: Decorator protects expense routes
- **User Ownership Check**: Ensures users can only access their own expenses
- **CSRF Protection**: All forms include CSRF tokens

## 🗄️ Database Structure

### Models (model.py)

#### User Model
```python
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique)
    email = db.Column(db.String(120), nullable=False, unique)
    password = db.Column(db.String(256), nullable=False)
```

**Features:**
- Password hashing using Werkzeug's `generate_password_hash`
- Password verification with `check_password_hash`
- Flask-Login integration via `UserMixin`

#### Expense Model
```python
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category = db.Column(db.String(50), nullable=False)
```

**Features:**
- Foreign key relationship to User model
- Automatic timestamp tracking
- Category-based organization
- User-specific data isolation

### Database Migrations

The application uses **Alembic** for database migrations:
- **Initial Migration**: Creates user and expense tables
- **Password Column Migration**: Increased password column length for better security
- **Version Control**: All schema changes tracked in `migrations/versions/`

### Database Operations

**CRUD Operations:**
- **Create**: `db.session.add()` and `db.session.commit()`
- **Read**: `Model.query.filter_by()`, `Model.query.get_or_404()`
- **Update**: Direct attribute assignment with commit
- **Delete**: `db.session.delete()` with commit

**Query Features:**
- Aggregation: `func.sum()` for total calculation
- Filtering: User-specific data isolation
- Error Handling: 404 responses for missing resources

## 🌐 API Structure

### Route Pattern

The application follows a **RESTful-inspired** routing pattern:

```
GET    /                    → Homepage (redirects)
GET/POST /register          → User registration
GET/POST /login             → User authentication
GET    /logout              → User logout
GET    /expenses            → List expenses (protected)
GET/POST /expense/add       → Create expense (protected)
GET/POST /expense/update/<id> → Update expense (protected)
POST   /expense/delete/<id> → Delete expense (protected)
```

### API Call Flow

**1. User Registration Flow:**
```
Client → POST /register → RegisterForm validation → 
User creation → Password hashing → Database commit → 
Auto-login → Redirect to /expenses
```

**2. Expense Creation Flow:**
```
Client → POST /expense/add → ExpenseForm validation → 
Expense object creation → User association → Database commit → 
Flash message → Redirect to /expenses
```

**3. Expense List Flow:**
```
Client → GET /expenses → Authentication check → 
Query user expenses → Calculate total → 
Render template with data → Return HTML
```

### Data Flow Architecture

```
HTTP Request → Route Handler → Form Validation → 
Business Logic → Database Operation → Response/Redirect
```

**Security Measures:**
- CSRF tokens on all forms
- Password hashing (never stored in plain text)
- User ownership verification for expense operations
- Session-based authentication
- SQL injection prevention via ORM

## 🤝 Collaboration Opportunities

### Areas for Improvement

This project is actively seeking collaboration in the following areas:

#### 🔐 Security Enhancements
- **Email Verification**: Implement email confirmation for registration
- **Password Reset**: Add forgot password functionality
- **Two-Factor Authentication**: Optional 2FA for enhanced security
- **Rate Limiting**: Implement rate limiting to prevent brute force attacks
- **Session Management**: Add session timeout and concurrent session handling

#### 📊 Feature Additions
- **Expense Analytics**: Dashboard with charts and spending trends
- **Budget Management**: Set and track monthly budgets by category
- **Recurring Expenses**: Automated recurring expense tracking
- **Expense Categories**: Allow users to create custom categories
- **Export Functionality**: Export expenses to CSV/PDF
- **Import Functionality**: Bulk import from bank statements or CSV files
- **Search & Filtering**: Advanced search with date ranges and filters
- **Expense Splitting**: Split expenses between multiple users

#### 🎨 UI/UX Improvements
- **Dark Mode**: Add theme switching capability
- **Mobile App**: Progressive Web App (PWA) or native mobile app
- **Accessibility**: Improve WCAG compliance and screen reader support
- **Internationalization**: Multi-language support (i18n)
- **Currency Support**: Multi-currency handling with conversion rates

#### ⚡ Performance Optimization
- **Database Indexing**: Add indexes for frequently queried fields
- **Caching**: Implement Redis caching for expensive queries
- **Pagination**: Add pagination for large expense lists
- **API Optimization**: Create REST API for mobile/integration
- **Database Optimization**: Query optimization and N+1 prevention

#### 🧪 Testing & Quality
- **Unit Tests**: Add comprehensive unit tests for models and routes
- **Integration Tests**: End-to-end testing with Selenium/Playwright
- **CI/CD Pipeline**: GitHub Actions for automated testing and deployment
- **Code Quality**: Implement linting (flake8, black) and pre-commit hooks
- **Documentation**: API documentation with Swagger/OpenAPI

#### 🚀 DevOps & Deployment
- **Docker**: Containerize the application for easier deployment
- **Kubernetes**: K8s manifests for scaling
- **Monitoring**: Add application monitoring (Sentry, New Relic)
- **Logging**: Structured logging with log rotation
- **Backup Strategy**: Automated database backups

#### 📱 Third-Party Integrations
- **Payment Gateway**: Connect to bank APIs for automatic expense import
- **Calendar Integration**: Sync expenses with calendar apps
- **Notification System**: Email/SMS alerts for budget limits
- **Social Sharing**: Share expense reports (optional)

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Saad Ahmad - Initial work

## 🙏 Acknowledgments

- Flask framework and its ecosystem
- WTForms for form handling
- Google Fonts for the beautiful handwritten fonts
- The open-source community

---

**Note**: This is a personal project and is not affiliated with any commercial service. Use it responsibly and ensure proper security measures are in place for production use.